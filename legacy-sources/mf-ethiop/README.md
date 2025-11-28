# Metafont (`.mf`) Sources from the LaTeX `ethiop` Package

These sources come from the CTAN `ethiop` package: [https://ctan.org/pkg/ethiop](https://ctan.org/pkg/ethiop)


# Running mf on a Mac M1

If this error is encountered when running `mf`:

```
'/opt/X11/lib/libSM.6.dylib' (fat file, but missing compatible architecture (have 'i386,x86_64', need 'arm64e' or 'arm64e.v1' or 'arm64' or 'arm64')), '/usr/lib/libSM.6.dylib' (no such file, not in dyld cache)o
```

It is a conflict between `x86` chip architecture of older MacBooks and the `M` series chipset. A TeX distribution may have been compiled against the
older archicture.  To get around the issue, install rosetta 2, ala:

```
softwareupdate --install-roset
```

Then, to force the `x86x context for a shell session, launch the shell as per:

```
arch -x86_64 zsh
```
