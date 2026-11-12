# 🎅 Pwning Santa before the bad guys do 🎄

**tl;dr:** Craft a document that breaks out of Dangerzone's sandbox, capture
one of the three flags we plant during the conversion, and earn up to
**$3,000** 💰. Encrypt your document with [Kenny's age key](kenny.pub), send it
as `letter.age` in a PR, and our CI job will do the rest.

## 📜 The backstory

Once upon a time, Santa Claus received letters from children all over the world,
delivered by trusty postal workers. But times have changed! With kids more
online than ever, Santa had to adapt and start opening letters in digital form.

Enter **Kenny Longears**, an elf in Santa's security team (yes, Virginia, Santa
has one)! 🧝 Kenny always preferred the ol' paper format. That way, he didn't
need to worry about worms, bugs, and other pests that have no place in the North
Pole. Begrudgingly, he yielded to the new era and set up
[Dangerzone](https://dangerzone.rocks/) in Santa's laptop to safely open email
attachments. But wait! Kenny, being the cautious elf he is, decided to
challenge Santa's red team to find vulnerabilities in Dangerzone before the
naughty hackers do.

## 🕵️ The challenge

Craft a _naughty_ letter that can demonstrably bypass some or all of
Dangerzone's defenses and earn a bounty 💰.

> [!TIP]
> New to Dangerzone? Read
> [how Dangerzone works](https://docs.dangerzone.rocks/latest/explanation/how-dangerzone-works/)
> and our
> [security model](https://docs.dangerzone.rocks/latest/explanation/security-model/)
> first.

To demonstrate your attack, you can send a PR to this repo with a specially
crafted document, and a [CI job](.github/workflows/submit.yml) will
sanitize it with Dangerzone. The catch here is that this CI job plants **three**
flags in the following locations:

1. **The sandbox where the document turns into pixels**
   (`/home/dangerzone/raster.flag` within the gVisor sandbox).
2. **The container that spawns the gVisor sandbox for the conversion**
   (`/gvisor.flag` within the Podman container).
3. **The host of the CI job, where Dangerzone is installed**
   (`~/secrets/host.flag` file in the host).

If you manage to capture one or more of these flags, add them in the sanitized
document or print them to stderr from the conversion sandbox. The CI job will
detect it, and the submission will be considered a success.

## 💰 The bounty

Capturing a flag varies in difficulty. Dangerzone
[assumes](https://docs.dangerzone.rocks/latest/explanation/security-model/)
that attackers can find vulnerabilities in the programs we use for rasterization
(LibreOffice and PyMuPDF). Therefore, the `raster.flag` is expected to be
captured at some point. The `gvisor.flag` flag requires escaping the gVisor
sandbox, which is much, _much_ more difficult. And the `host.flag` flag
requires combining a gVisor sandbox escape and a Linux container escape at the
same time, which we haven't seen yet in the wild.

Each flag is backed by a bounty, and the first PR that captures it gets that
bounty 🤑. The bounty levels are:

1. 🥇 `~/secrets/host.flag` in the host: **$1,700.**
2. 🥈 `/gvisor.flag` within the Podman container: **$1,000.**
3. 🥉 `/home/dangerzone/raster.flag` within the gVisor sandbox: **$300.**

A PR can capture multiple flags at once, in which case it can get the full
bounty, i.e., **$3,000**. Note that each flag can be captured once, since we
need to cap the total payout to **$3,000** across all submissions. In case of
multiple submissions that capture the same flag, the first one wins 🏁.

## 🧙 Get started

1. Fork this repo.
2. Craft your document (see
   [supported formats](https://docs.dangerzone.rocks/latest/reference/supported-formats/))
   with the payload in it.
3. Encrypt the document using [Kenny's public key](kenny.pub). You will need
   [age](https://age-encryption.org) for that:

   ```shell
   age --encrypt --recipients-file kenny.pub --output letter.age ./letter
   ```

4. Add `letter.age` in the root of the repo. This must be the **only** file
   that your PR changes, else the CI job will reject it.
5. Submit a PR and let the games begin! 🥳

## ❓ FAQ

### 1. Why do we encrypt documents when we submit them?

There are two primary reasons for encrypting your submissions. First, this is a
public challenge, and we want to protect your ideas from being copied by others.
Second, and more importantly, we aim to prevent real-world attackers from
observing potential exploits and targeting our users. Encryption helps maintain
the integrity and security of the challenge.

### 2. What happens on a successful submission?

If your submission is successful, we will redirect you to our
[Bugcrowd account](https://bugcrowd.com/engagements/freedomofpress)
to receive your reward. At the same time though, you will own the exploit. We
will assist you in reaching out to the affected parties and help you claim any
additional bounties they may offer for the vulnerability.

### 3. Can I experiment with this challenge locally?

Absolutely! You are encouraged to
[install Dangerzone](https://docs.dangerzone.rocks/latest/how-to/install/)
locally and experiment with creating a document that can read a file from your
PC during the sanitization process. Check out our
[CI job](.github/workflows/submit.yml) and [`dz.patch`](dz.patch) as well, to
see how we plant the flags for the challenge, and our
[sandbox debugging guide](https://docs.dangerzone.rocks/latest/how-to/contribute/debug-the-sandbox/)
to see what happens within the sandbox. Once you have crafted your document,
feel free to submit the encrypted version as a PR. Happy experimenting!

### 4. Does my submission have to pass the sanitization step?

If your submission cannot be sanitized, this means that we can't check for the
captured flag in the resulting document. That's not a problem, though, since we
look for flags in the conversion logs as well. If you capture a flag, you can
print it to the process' stderr, and it will be included in the conversion logs.
You should see it in the output of the CI job as well.

### 5. Can I submit any other types of issues?

If they undermine Dangerzone's security, you are encouraged to submit them via
our [Bugcrowd account](https://bugcrowd.com/engagements/freedomofpress), and we
_may_ assign a payout according to their severity, e.g., what flag they would
potentially capture.

If they target this CI job, then they are considered out of scope.

### 6. Are we living in such desperate times that people will burn a gVisor/kernel 0-day for anything less than six figures?

Of course not! We are living in the merriest of times, where people can
contribute their talent to spyware companies, enjoy a big payout, and sleep
soundly at night! But at the same time, and let's be real for a second, no one
will waste six figures to break Dangerzone. And if they do, this means that
Dangerzone will have succeeded in protecting all the rest of the users that are
not economically viable targets.

The scenario we want to avoid, though, is having a bug lying around that makes
it trivial to bypass the defense layers Dangerzone employs. That's what we're
looking for here, and the sanitization logic, for that matter, is pretty small.
So, hopefully, this bounty will incentivize some folks to give our repo a look.

### 7. Is this a CTF challenge, or a bug bounty program?

It's a capped bug bounty program. The backstory is this: Dangerzone has never
had a bug bounty program,
[as its sister project, SecureDrop, has](https://bugcrowd.com/engagements/freedomofpress).
Our team has managed to secure some money from the bug bounty pool that was not
spent this year and decided to give a festive spin to it because, well, why not?
We hope that at some point in the future, we'll have an actual bug bounty
program in place.
