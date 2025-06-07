# Security Policy

## Supported Versions

The following table outlines the versions of this project currently supported with security updates:

| Version | Supported |
|---------|-----------|
| Latest  | ✅ Yes    |
| Older   | ❌ No     |

---

## Reporting a Vulnerability

We take the security of this project seriously. If you discover a vulnerability, we kindly request that you report it **privately and responsibly**.

### 🔐 Please contact:
**Email:** [dhruvjain5130@outlook.com](mailto:dhruvjain5130@outlook.com)

To help us respond faster, please include:
- A clear description of the issue
- Steps to reproduce the vulnerability
- A proof of concept (if available)
- Any relevant logs or screenshots

---

## Response Process

We aim to:
- Acknowledge receipt of your report within **48 hours**
- Provide an initial assessment within **72 hours**
- Roll out a fix for verified vulnerabilities within **7 business days**
- Credit contributors who report valid issues (with consent)

All reports are reviewed manually, and we maintain confidentiality throughout the process.

---

## Security Measures in Place

The project implements the following security practices:

- 🔐 Code reviews for all pull requests
- ✅ GitHub branch protection with required status checks
- 🔁 Enforced linear git history (no merge commits)
- 🧪 Continuous Integration (CI) with automated testing and linting
- 🔑 Sensitive credentials handled via environment variables (`.env`)
- ❌ No direct database writes from the frontend
- 🔍 Regular dependency updates and vulnerability scans

---

## Scope

This policy applies to:
- All code and services maintained in this repository
- The PyQt GUI frontend and any backend logic in Python
- MySQL database logic related to user authentication, team data, and scoring

The policy **does not cover**:
- Third-party services used in conjunction with this app
- Any forks or modified versions outside this repository

---

## Acknowledgments

We appreciate and recognize contributions from the community that improve the security and reliability of this project. If you’re reporting a valid issue, we’re happy to offer credit in release notes or the repository’s contributors list (if you choose).

---

## Thank You 🙏

Your efforts to responsibly disclose and help fix security vulnerabilities are invaluable.  
Let’s build something safer — together.

