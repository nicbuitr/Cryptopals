<p align="center">
   <a href="https://cryptopals.com/">
     <img src="https://cryptoservices.github.io/images/ncc-logo.png">
     <h1 align="center">Cryptopals</h1>
  </a>
</p>

<p align="center">
    <a href="https://github.com/shivakaushal/Cryptopals/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/shivakaushal/Cryptopals.svg" alt="Build Status">
    </a>
    <a href="https://github.com/xXH4CKST3RXx/JS-Neural-Networks-Course/">
        <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" alt="Build Status">
    </a>
</p>

# Introduction

This repository contains the source code of the collection of 64 exercises that demonstrate attacks on real-world crypto, these are split in 8 sets of challenges as displayed at the [Cryptopals Website](https://cryptopals.com/).

This is a different way to learn about crypto than taking a class or reading a book. We give you problems to solve. They're derived from weaknesses in real-world systems and modern cryptographic constructions. We give you enough info to learn about the underlying crypto concepts yourself. When you're finished, you'll not only have learned a good deal about how cryptosystems are built, but you'll also understand how they're attacked.

## What Are The Rules?
There aren't any! For several years, we ran these challenges over email, and asked participants not to share their results. The honor system worked beautifully! But now we're ready to set aside the ceremony and just publish the challenges for everyone to work on.

## How Much Math Do I Need To Know?
If you have any trouble with the math in these problems, you should be able to find a local 9th grader to help you out. It turns out that many modern crypto attacks don't involve much hard math.

## How Much Crypto Do I Need To Know?
None. That's the point.

So What Do I Need To Know?
You'll want to be able to code proficiently in any language. We've received submissions in C, C++, Python, Ruby, Perl, Visual Basic, X86 Assembly, Haskell, and Lisp. Surprise us with another language. Our friend Maciej says these challenges are a good way to learn a new language, so maybe now's the time to pick up Clojure or Rust.

## What Should I Expect?
Right now, we have eight sets. They get progressively harder. Again: these are based off real-world vulnerabilities. None of them are "puzzles". They're not designed to trip you up. Some of the attacks are clever, though, and if you're not familiar with crypto cleverness... well, you should like solving puzzles. An appreciation for early-90's MTV hip-hop can't hurt either.

## Can You Give Us A Long-Winded Indulgent Description For Why You'Ve Chosen To Do This?
_It turns out that we can._

If you're not that familiar with crypto already, or if your familiarity comes mostly from things like Applied Cryptography, this fact may surprise you: most crypto is fatally broken. The systems we're relying on today that aren't known to be fatally broken are in a state of just waiting to be fatally broken. Nobody is sure that TLS 1.2 or SSH 2 or OTR are going to remain safe as designed.

The current state of crypto software security is similar to the state of software security in the 1990s. Specifically: until around 1995, it was not common knowledge that software built by humans might have trouble counting. As a result, nobody could size a buffer properly, and humanity incurred billions of dollars in cleanup after a decade and a half of emergency fixes for memory corruption vulnerabilities.

Counting is not a hard problem. But cryptography is. There are just a few things you can screw up to get the size of a buffer wrong. There are tens, probably hundreds, of obscure little things you can do to take a cryptosystem that should be secure even against an adversary with more CPU cores than there are atoms in the solar system, and make it solveable with a Perl script and 15 seconds. Don't take our word for it: do the challenges and you'll see.

People "know" this already, but they don't really know it in their gut, and we think the reason for that is that very few people actually know how to implement the best-known attacks. So, mail us, and we'll give you a tour of them.

## How do I start?
[Start here!](https://cryptopals.com/sets/1)

## Built with:

[![HTML](https://github.com/nicbuitr/f/blob/master/python.png)](https://www.python.org/) |
:---:|

## Contributors

Thanks to all the people who have improved this repository!

<a href="https://github.com/shivakaushal/Cryptopals/graphs/contributors">
  <img src="https://contributors-img.firebaseapp.com/image?repo=shivakaushal/Cryptopals" />
</a>

Made with [Contributors IMG](https://contributors-img.firebaseapp.com).

## Who did this?

- Thomas Ptacek (@tqbf)
- Sean Devlin (@spdevlin)
- Alex Balducci (@iamalexalright)
- Marcin Wielgoszewski (@marcinw)

Cryptopals is maintained and expanded (from Set 8 on) by Sean Devlin, in conjunction with the [Cryptography Services Team](https://www.nccgroup.trust/us/our-services/security-consulting/cryptography-services/) at [NCC Group](https://www.nccgroup.trust/us/).

We could not possibly have done this without the help of several other people. Roughly in order of influence:

[Nate Lawson](http://www.rootlabs.com/) taught us virtually everything we know about cryptography.
[Trevor Perrin](http://trevp.net/) taught Nate some of that. I can tell you a pretty compelling story about how Trevor is the intellectual origin of every successful attack on TLS over the past 5 years.
Thai Duong and Juliano Rizzo are the godfathers of practical cryptographic software security. Several things in this challenge didn't make sense to us until after Thai and Juliano exploited them in mainstream software.

## License

MIT

## Legal

Individual exercise submissions are owned by their author, and may or may not be distributed under an open source license.

[Cryptography Services](https://cryptoservices.github.io/) | [NCC Group](https://www.nccgroup.trust/us/)
