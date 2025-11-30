from storage_virtual_network import StorageVirtualNetwork
from storage_virtual_node import StorageVirtualNode
import time

# Create network
network = StorageVirtualNetwork()

# Create nodes with > 2TB storage
node1 = StorageVirtualNode("node1", cpu_capacity=8, memory_capacity=32, storage_capacity=3000, bandwidth=1000)
node2 = StorageVirtualNode("node2", cpu_capacity=16, memory_capacity=64, storage_capacity=4000, bandwidth=2000)
node3 = StorageVirtualNode("node3", cpu_capacity=8, memory_capacity=32, storage_capacity=3000, bandwidth=1000)

# Add nodes to network
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)

# Connect nodes: node1 <-> node2 <-> node3
# This forces traffic from node1 to node3 to go through node2
network.connect_nodes("node1", "node2", bandwidth=1000)
network.connect_nodes("node2", "node3", bandwidth=1000)

print("Network Topology:")
print(f"Node 1 ({node1.ip_address}) <-> Node 2 ({node2.ip_address}) <-> Node 3 ({node3.ip_address})")

# Initiate file transfer (500MB file from node1 to node3)
transfer = network.initiate_file_transfer(
    source_node_id="node1",
    target_node_id="node3",
    file_name="huge_dataset.iso",
    file_size=500 * 1024 * 1024  # 500MB
)

if transfer:
    print(f"\nTransfer initiated: {transfer.file_id}")
    print(f"Source: {node1.node_id} ({node1.ip_address})")
    print(f"Target: {node3.node_id} ({node3.ip_address})")
    
    # Process transfer in chunks
    total_chunks = len(transfer.chunks)
    transferred_chunks = 0
    
    # simple ASCII progress
    def show_progress(done, total):
        pct = done / total
        bar_len = 40
        filled_len = int(pct * bar_len)
        bar = '█' * filled_len + '-' * (bar_len - filled_len)
        print(f"\rProgress: |{bar}| {done}/{total} chunks ({pct*100:.1f}%)", end='')

    start_time = time.time()
    
    while True:
        chunks_done, completed = network.process_file_transfer(
            source_node_id="node1",
            target_node_id="node3",
            file_id=transfer.file_id,
            chunks_per_step=5  # Process 5 chunks at a time
        )

        transferred_chunks += chunks_done
        if transferred_chunks > total_chunks:
            transferred_chunks = total_chunks

        show_progress(transferred_chunks, total_chunks)

        if completed:
            print()  # newline after progress
            duration = time.time() - start_time
            print(f"Transfer completed successfully in {duration:.2f} seconds!")
            break
            
        # Small sleep to make animation visible
        time.sleep(0.1)

    # Final stats
    print("\nFinal Statistics:")
    stats = network.get_network_stats()
    print(f"Total Network Storage: {stats['total_storage_bytes'] / (1024**3):.2f} GB")
    print(f"Used Storage on Node 3: {node3.used_storage / (1024**2):.2f} MB")
