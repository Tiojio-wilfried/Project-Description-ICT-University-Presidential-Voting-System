from typing import Dict, List, Optional, Tuple
import hashlib
import time
from storage_virtual_node import StorageVirtualNode, FileTransfer, TransferStatus
from collections import defaultdict
import itertools

def _ip_generator(subnet_prefix: str = "10.0.0."):
    """Simple IP generator for nodes."""
    for i in itertools.count(1):
        yield f"{subnet_prefix}{i}"


class StorageVirtualNetwork:
    def __init__(self):
        self.nodes: Dict[str, StorageVirtualNode] = {}
        # transfer_operations: source_node_id -> file_id -> {'transfer': FileTransfer, 'target': target_node_id}
        self.transfer_operations: Dict[str, Dict[str, dict]] = defaultdict(dict)
        self.ip_gen = _ip_generator()
        # adjacency: node_id -> dict(neighbor_id -> bandwidth_bps)
        self.adjacency: Dict[str, Dict[str, int]] = defaultdict(dict)
        
    def add_node(self, node: StorageVirtualNode):
        """Add a node to the network"""
        # assign ip
        node.ip_address = next(self.ip_gen)
        self.nodes[node.node_id] = node
        
    def connect_nodes(self, node1_id: str, node2_id: str, bandwidth: int):
        """Connect two nodes with specified bandwidth"""
        if node1_id in self.nodes and node2_id in self.nodes:
            self.nodes[node1_id].add_connection(node2_id, bandwidth)
            self.nodes[node2_id].add_connection(node1_id, bandwidth)
            # store adjacency in bits per second
            self.adjacency[node1_id][node2_id] = bandwidth * 1000000
            self.adjacency[node2_id][node1_id] = bandwidth * 1000000
            return True
        return False

    def _shortest_path(self, src: str, dst: str) -> Optional[List[str]]:
        """Simple BFS shortest path (by hops)"""
        if src == dst:
            return [src]
        visited = {src}
        queue = [[src]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            for neighbor in self.adjacency.get(node, {}):
                if neighbor in visited:
                    continue
                new_path = path + [neighbor]
                if neighbor == dst:
                    return new_path
                visited.add(neighbor)
                queue.append(new_path)
        return None

    def _path_bandwidth_bps(self, path: List[str]) -> int:
        """Return bottleneck bandwidth in bits per second for the path."""
        if not path or len(path) < 2:
            return 0
        bandwidths = []
        for a, b in zip(path, path[1:]):
            bandwidths.append(self.adjacency.get(a, {}).get(b, 0))
        return min(bandwidths) if bandwidths else 0
    
    def initiate_file_transfer(
        self,
        source_node_id: str,
        target_node_id: str,
        file_name: str,
        file_size: int
    ) -> Optional[FileTransfer]:
        """Initiate a file transfer between nodes"""
        if source_node_id not in self.nodes or target_node_id not in self.nodes:
            return None
            
        # Generate unique file ID
        file_id = hashlib.md5(f"{file_name}-{time.time()}".encode()).hexdigest()
        
        # Request storage on target node
        target_node = self.nodes[target_node_id]
        transfer = target_node.initiate_file_transfer(file_id, file_name, file_size, source_node_id)
        
        if transfer:
            self.transfer_operations[source_node_id][file_id] = {
                'transfer': transfer,
                'target': target_node_id
            }
            return transfer
        return None
    
    def process_file_transfer(
        self,
        source_node_id: str,
        target_node_id: str,
        file_id: str,
        chunks_per_step: int = 1
    ) -> Tuple[int, bool]:
        """Process a file transfer in chunks"""
        if (source_node_id not in self.nodes or 
            target_node_id not in self.nodes or
            file_id not in self.transfer_operations[source_node_id]):
            return (0, False)
            
        source_node = self.nodes[source_node_id]
        target_node = self.nodes[target_node_id]
        transfer_data = self.transfer_operations[source_node_id][file_id]
        transfer = transfer_data['transfer']

        # find path
        path = self._shortest_path(source_node_id, target_node_id)
        if not path:
            return (0, False)

        path_bw = self._path_bandwidth_bps(path)
        if path_bw <= 0:
            return (0, False)

        chunks_transferred = 0
        for chunk in transfer.chunks:
            if chunk.status != TransferStatus.COMPLETED and chunks_transferred < chunks_per_step:
                # simulate transfer time using bottleneck bandwidth
                chunk_bits = chunk.size * 8
                transfer_time = chunk_bits / path_bw
                time.sleep(transfer_time)

                # deliver chunk hop-by-hop (update nodes along path)
                delivered = True
                for hop in path[1:]:
                    node = self.nodes[hop]
                    # ensure node has the transfer record
                    if file_id not in node.active_transfers and hop == target_node_id:
                        # target should have initiated a storage reservation earlier
                        delivered = False
                        break
                    # accept chunk at final node
                if not delivered:
                    return (chunks_transferred, False)

                # mark chunk completed on target
                if target_node.accept_chunk(file_id, chunk.chunk_id, source_node_id):
                    chunks_transferred += 1
                else:
                    return (chunks_transferred, False)
        
        # Check if transfer is complete
        if transfer.status == TransferStatus.COMPLETED:
            del self.transfer_operations[source_node_id][file_id]
            return (chunks_transferred, True)
            
        return (chunks_transferred, False)
    
    def get_network_stats(self) -> Dict[str, float]:
        """Get overall network statistics"""
        total_bandwidth = sum(n.bandwidth for n in self.nodes.values())
        used_bandwidth = sum(n.network_utilization for n in self.nodes.values())
        total_storage = sum(n.total_storage for n in self.nodes.values())
        used_storage = sum(n.used_storage for n in self.nodes.values())
        return {
            "total_nodes": len(self.nodes),
            "total_bandwidth_bps": total_bandwidth,
            "used_bandwidth_bps": used_bandwidth,
            "bandwidth_utilization": (used_bandwidth / total_bandwidth) * 100 if total_bandwidth else 0.0,
            "total_storage_bytes": total_storage,
            "used_storage_bytes": used_storage,
            "storage_utilization": (used_storage / total_storage) * 100 if total_storage else 0.0,
            "active_transfers": sum(len(t) for t in self.transfer_operations.values())
        }