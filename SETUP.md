# Development Environment Setup Guide

This guide will help you set up your development environment for the ICT University Presidential Voting System project, including how to sign in to GitHub Copilot in Visual Studio Code.

## Prerequisites

- A GitHub account
- Visual Studio Code installed on your computer
- Git installed on your computer

## Installing Visual Studio Code

If you haven't installed Visual Studio Code yet:

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download the version for your operating system (Windows, macOS, or Linux)
3. Run the installer and follow the installation instructions
4. Launch Visual Studio Code after installation

## Setting Up GitHub Copilot in VSCode

GitHub Copilot is an AI-powered code completion tool that can help you write code faster and more efficiently.

### Step 1: Install the GitHub Copilot Extension

1. Open Visual Studio Code
2. Click on the Extensions icon in the left sidebar (or press `Ctrl+Shift+X` on Windows/Linux or `Cmd+Shift+X` on macOS)
3. In the search bar, type "GitHub Copilot"
4. Find "GitHub Copilot" by GitHub (the official extension)
5. Click the "Install" button

### Step 2: Sign In to GitHub Copilot

After installing the extension, you need to authenticate:

1. **Automatic Sign-In Prompt:**
   - VSCode may automatically prompt you to sign in to GitHub
   - Click "Sign in to GitHub" when prompted

2. **Manual Sign-In:**
   If you don't see an automatic prompt:
   - Click on the Accounts icon in the bottom left corner of VSCode (it looks like a person silhouette)
   - Select "Sign in with GitHub to use GitHub Copilot"
   - Alternatively, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
   - Type "GitHub Copilot: Sign In" and press Enter

3. **Authorization Process:**
   - VSCode will open your default web browser
   - You'll be redirected to GitHub's authorization page
   - Click "Authorize Visual-Studio-Code" to allow VSCode to access your GitHub account
   - You may be prompted to enter your GitHub password for confirmation
   - After authorization, you'll see a success message
   - Return to VSCode

4. **Verify Your Subscription:**
   - GitHub Copilot requires an active subscription or access through an organization
   - If you're a student, you can get free access through [GitHub Education](https://education.github.com/)
   - If you're part of an organization with Copilot access, ensure you're signed in with the correct account

### Step 3: Verify Installation

To verify that GitHub Copilot is working:

1. Create a new file in VSCode (e.g., `test.py` or `test.js`)
2. Start typing a function or comment describing what you want to do
3. GitHub Copilot should show suggestions in gray text
4. Press `Tab` to accept a suggestion or `Esc` to dismiss it

Example:
```python
# Function to calculate the sum of two numbers
# Start typing this comment, and Copilot should suggest the function implementation
```

### Troubleshooting

**Issue: GitHub Copilot is not showing suggestions**

- Check the status bar at the bottom of VSCode for a GitHub Copilot icon
- Click on the icon to see the status (should show a checkmark if active)
- Ensure you're signed in correctly by checking the Accounts section
- Try reloading VSCode: `Ctrl+Shift+P` → "Developer: Reload Window"

**Issue: "GitHub Copilot could not connect to server"**

- Check your internet connection
- Verify that your GitHub Copilot subscription is active
- Sign out and sign back in: `Ctrl+Shift+P` → "GitHub Copilot: Sign Out" then sign in again

**Issue: Authorization failed**

- Make sure you're signed in to the correct GitHub account in your browser
- Clear your browser cache and try the authorization process again
- Check if your organization has specific policies that might block Copilot access

**Issue: Subscription or access required**

- Visit [https://github.com/features/copilot](https://github.com/features/copilot) to sign up
- Students and educators can get free access through GitHub Education
- Check with your organization if they provide Copilot access

## Additional Recommended Extensions for VSCode

For the ICT University Voting System project, you might also want to install:

- **Python** (if using Python)
- **ESLint** (if using JavaScript)
- **Prettier** - Code formatter
- **GitLens** - Enhanced Git capabilities
- **Live Share** - Real-time collaborative coding

## Getting Started with the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/Tiojio-wilfried/Project-Description-ICT-University-Presidential-Voting-System.git
   ```

2. Open the project folder in VSCode:
   ```bash
   cd Project-Description-ICT-University-Presidential-Voting-System
   code .
   ```

3. Review the project documentation in `ICT_University_Voting_System_Project.pdf`

4. Start coding with GitHub Copilot assistance!

## Using GitHub Copilot Effectively

### Tips for Better Suggestions:

1. **Write clear comments:** Describe what you want the code to do
2. **Use descriptive variable names:** Helps Copilot understand context
3. **Provide examples:** Show Copilot the pattern you want to follow
4. **Accept and modify:** Don't accept every suggestion blindly - review and adapt

### Keyboard Shortcuts:

- `Tab` - Accept suggestion
- `Esc` - Dismiss suggestion
- `Alt+]` or `Option+]` - Next suggestion
- `Alt+[` or `Option+[` - Previous suggestion
- `Ctrl+Enter` - Open Copilot suggestions panel

## Support and Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VSCode Documentation](https://code.visualstudio.com/docs)
- [GitHub Education](https://education.github.com/) - For free student access

## Contributing

Once you have your environment set up, you can start contributing to the ICT University Presidential Voting System project. Please follow the coding standards and guidelines that will be established as the project develops.

---

*Last updated: November 2025*
