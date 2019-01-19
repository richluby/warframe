# libWarframe

This library provides the capability to test various warframe statistics,
builds, and affects. Contributions are welcome.

# Overview

As it is python, most elements are represented as a class. All warframes
inherit from the default `Warframe` class. This class provides a single
structure around which to build warframes. The intent is NOT to provide mod
interactions, but rather to demonstrate the end result of the modding process.
In other words, this library allows calculating warframe statistics given the
results of mods. It is out of scope of the library to track mods and their
individual effects on the game.

