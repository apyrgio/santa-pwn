# 🎅 Pwning Santa before the bad guys do 🎄

Welcome to the merriest cyber security challenge this side of the North Pole! 🎁

## 📜 The Backstory

Once upon a time, Santa Claus received letters from children all over the world, delivered by trusty postal workers. This was not just a charming tradition; paper can't hack you. But times have changed! With kids more online than ever and their parents used to sending emails faster than you can say "Ho Ho Ho," Santa had to adapt and start opening letters in digital form.

Enter **Kenny Longears**, an elf in Santa's security team (yes Virginia, Santa has one)! 🧝 Kenny suggested that Santa use **Dangerzone** to safely open email attachments. But wait! Kenny, being the cautious elf he is, decided to challenge Santa's red team to find vulnerabilities in Dangerzone before the naughty hackers do.

## 🕵️ The Challenge

This GitHub repo is your playground! It contains a [CI job](https://github.com/apyrgio/santa-pwn/blob/main/.github/workflows/submit.yml) which accepts a document, and sanitizes it with **Dangerzone**. Your mission, should you choose to accept it, is to craft a document that can extract hidden secrets from the following locations:

- **The sandbox where the sanitization takes place:** (flag in `/rasterizer` file within the gVisor sandbox)
- **The container that spawns the gVisor sandbox for the conversion:** (flag in `/gvisor` file within the Podman container)
- **The host of the CI job, where Dangerzone is installed:** (flag in `~/secrets/host` file in the host)

If you have captured one or more of these flags, add it in your document while rasterization runs. The CI job is checking for the flags in the sanitized document, and so the tests will pass.

Capturing a flag varies in difficulty. Dangerzone operates under the assumption that attackers can find vulnerabilities in the programs we use for rasterization (LibreOffice and PyMuPDF). Therefore, the `/rasterizer` flag is expected to be captured at some point. The `/gvisor` flag requires escaping the gVisor sandbox, which is much more difficult, and the `~/secrets/host` flag requires combining a gVisor sandbox escape, and a Linux container escape, at the same time, which we haven't seen yet in the wild.

The first PR that successfully retrieves one of these secrets will earn a **bounty**! 🎉 (bounty levels TBD)

## 📜 Submission Terms

Before you dive in, here are the rules of engagement:

1. **No Attacking the GitHub Action Workflow:** This is a friendly challenge, not a full-blown cyber war! Focus on the document crafting.
2. **Encrypt Your Submissions:** All documents must be submitted as encrypted files (`/letter.gpg`) using Kenny's public key. [🔑 Get Kenny's Public Key Here!](https://github.com/apyrgio/santa-pwn/blob/main/kenny.asc)
3. **Document Types:** Feel free to use any document types that Dangerzone accepts.

## 🎁 What’s at Stake?

Not only will you earn the coveted bounty, but you'll also gain the eternal gratitude of Santa and his elves! Plus, you’ll be helping to keep the North Pole safe from cyber threats. 🎅✨

## 🧙 Get Started

1. Fork this repo.
2. Craft your document with the payload in it.
3. Encrypt it using Kenny's public key.
4. Submit a PR and let the games begin!

May your creativity flow like hot cocoa on a winter's night! Good luck, and may the best elf win! 🥳

## ❓ FAQ

### 1. Why do we encrypt documents when we submit them?
**Answer:** There are two primary reasons for encrypting your submissions. First, this is a public challenge, and we want to protect your ideas from being copied by others. Second, and more importantly, we aim to prevent real-world attackers from observing potential exploits and using them against our users. Encryption helps maintain the integrity and security of the challenge.

### 2. What happens on a successful submission?
**Answer:** If your submission is successful, you will own the exploit. We will assist you in reaching out to the affected parties and help you claim any additional bounties they may offer for the vulnerability.

### 3. Can I experiment with this challenge locally?
**Answer:** Absolutely! You are encouraged to install Dangerzone locally and experiment with creating a document that can read a file from your PC during the sanitization process. Check out our [CI job](https://github.com/apyrgio/santa-pwn/blob/main/.github/workflows/submit.yml) as well to see how we plant the flags for the challenge. Once you have crafted your document, feel free to submit the encrypted version as a PR. Happy experimenting!

---

*Disclaimer: This challenge is purely for educational and entertainment purposes. No elves were harmed in the making of this repo.*
