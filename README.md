# 🎅 Pwning Santa before the bad guys do 🎄

Welcome to the merriest cyber security challenge this side of the North Pole! 🎁

## 📜 The Backstory

Once upon a time, Santa Claus received letters from children all over the world, delivered by trusty postal workers. But times have changed! With kids more online than ever and their parents used to sending emails faster than you can say "Ho Ho Ho," Santa had to adapt and start opening letters in digital form.

Enter **Kenny Longears**, an elf in Santa's security team (yes Virginia, Santa has one)! 🧝 Kenny always preferred the ol' paper format, because he wouldn't need to worry about worms, bugs, and other pests that have no place in the North Pole. Begrudgingly, he yielded to the new era, and set up [Dangerzone](https://dangerzone.rocks/) in Santa's laptop, to safely open email attachments. But wait! Kenny, being the cautious elf he is, decided to challenge Santa's red team to find vulnerabilities in Dangerzone before the naughty hackers do.

## 🕵️ The Challenge

This GitHub repo is your playground! It contains a [CI job](.github/workflows/submit.yml) which accepts a document, and sanitizes it with **Dangerzone**. Your mission, should you choose to accept it, is to craft a document that can extract hidden secrets from the following locations:

- **The sandbox where the sanitization takes place:** (`/home/dangerzone/raster.flag` within the gVisor sandbox)
- **The container that spawns the gVisor sandbox for the conversion:** (`/gvisor.flag` within the Podman container)
- **The host of the CI job, where Dangerzone is installed:** (`~/secrets/host.flag` file in the host)

> [!TIP]
> Read more about Dangerzone's use of nested containers in an article we
> co-authored with the gVisor team:
> [Safe Ride into the Dangerzone: Reducing attack surface with gVisor](https://dangerzone.rocks/news/2024-09-23-gvisor/)

If you have captured one or more of these flags, add it in your document or print it to stderr, while rasterization runs. The CI job is checking for the flags in the sanitized document or the conversion logs, and so will detect the captured flag. Once that happens, the tests will pass and the submission will be considered a success.

Capturing a flag varies in difficulty. Dangerzone operates under the assumption that attackers can find vulnerabilities in the programs we use for rasterization (LibreOffice and PyMuPDF). Therefore, the `raster.flag` is expected to be captured at some point. The `gvisor.flag` flag requires escaping the gVisor sandbox, which is much, _much_ more difficult, and the `~/secrets/host` flag requires combining a gVisor sandbox escape, and a Linux container escape, at the same time, which we haven't seen yet in the wild.

Each flag is backed by a bounty, and the first PR that captures it, gets that bounty 🤑. The bounty levels are:
1. 🥇 `~/secrets/host.flag` in the host: **$1,700**
2. 🥈 `/gvisor.flag` within the Podman container: **$1,000**
3. 🥉 `/home/dangerzone/raster.flag` within the gVisor sandbox: **$300**

A PR can capture multiple flags at once, in which case it can get the full bounty, i.e., **$3,000**. Note that each flag can be captured once, since we need to cap the total payout to **$3,000** across all submissions. In case of multiple submissions that capture the same flag, the first one wins 🏎️.

## 📜 Submission Terms

Before you dive in, here are the rules of engagement:

1. **No Attacking the GitHub Action Workflow:** This is a friendly challenge, not a full-blown cyber war! Focus on the document crafting.
2. **Encrypt Your Submissions:** The document must be submitted as an encrypted file named `./letter.gpg`, using [Kenny's public key](kenny.asc):

   ```
   gpg --import < kenny.asc
   gpg --recipient kenny@santa.club --encrypt ./letter
   ```

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

### 4. Does my submission have to pass the sanitization step?
**Answer:** If your submission cannot be sanitized, this means that we can't
check for the captured flag in the resulting document. That's not a problem
though, since we look for flags in the conversion logs as well. If you capture a
flag, you can print to via the process' stderr, and it will be included in the
conversion logs. You should see it in the output of the CI job as well.

### 5. What if I find a security issue in a separate Dangerzone component that cannot manifest in this particular challenge?
**Answer:** You are encouraged to submit it via our Bug Crowd account, and we
can assign a payout according to its severity, e.g., what flag would it
potentially capture.

### 6. Are we living in such desperate times that people will burn a gVisor/kernel 0-day for anything less than seven figures?
**Answer:** Of course not! We are living in the merriest of times, where people can contribute their talent to spyware companies, enjoy a big payout, and sleep sound at night! But at the same time, and let's be real for a second, no one will waste seven figures to break Dangerzone. And if they do, this means that Dangerzone will have succeeded in protecting all the rest of the users that are not economically viable targets.

The scenario we want to avoid though is having a bug lying around that makes it trivial to bypass all of these hardened defense layers that Dangerzone employs. That's what we're looking for here, and the sanitization logic for that matter is pretty small. So hopefully, this bounty will incentivize some folks to give our repo a look.

### 7. I'm not sure I get it, is this a CTF chalenge, or a bug bounty program?
**Answer:** It's a capped bug bounty program. The backstory is this: Dangerzone
never had a bug bounty program as its sister project, SecureDrop, did. Our team
has managed to secure some money from the bug bounty pool that were not spent
this year, and decided to give an festive spin to it because, well, why not. We
hope that at some point in the future we'll have an actual bug bounty program
in place.

---

*Disclaimer: This challenge is purely for educational and entertainment purposes. No elves were harmed in the making of this repo.*
