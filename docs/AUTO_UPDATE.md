# Auto-updating the pack

The CI publishes the current pack in packwiz format to the `pack` branch on every push to `main`. A tool called packwiz-installer reads it and syncs your mods, shaders and configs before the game starts (adds new files, replaces changed ones, removes dropped ones).

Pack URL: `https://raw.githubusercontent.com/ManHazz/GT-Cataclysm/pack/pack.toml`

## Client (Prism Launcher)

1. Create a Forge 1.20.1 instance with Forge 47.4.13 (the versions listed in `pack.toml`). The installer does not change the Minecraft or Forge version, so keep them matched yourself.
2. Download `packwiz-installer-bootstrap.jar` from the [packwiz-installer-bootstrap releases](https://github.com/packwiz/packwiz-installer-bootstrap/releases) and put it in the instance's Minecraft folder (`.minecraft` or `minecraft`; use Folder > Minecraft Folder in Prism).
3. Edit instance > Settings > Custom commands, tick "Custom commands", and set Pre-launch command to:

   ```
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/ManHazz/GT-Cataclysm/pack/pack.toml
   ```

   Prism runs the command with the instance's Minecraft folder as working directory and provides `$INST_JAVA` (the instance's Java), so the relative jar name works.
4. Launch. The first launch opens an update window and downloads everything; later launches only fetch changes.

Notes:
- Do not put your own mods in `mods/` of this instance; the installer deletes files it previously installed when they leave the pack, but leaves unknown files alone.
- Files under `config/`, `kubejs/` and `patchouli_books/` are overwritten with the pack's version on change.
- Modrinth App is not supported (it has no pre-launch hook).

## Server

Use `server-template/start.bat`. Copy it into the server folder over the existing `start.bat`, and put `packwiz-installer-bootstrap.jar` next to it. Before each launch (including automatic restarts) it runs:

```
java -jar packwiz-installer-bootstrap.jar -g -s server <pack URL>
```

`-g` disables the GUI and `-s server` skips client-only mods. If the update fails, the script prints a warning and starts with the current files.

## Limitations

- packwiz has no per-file side for plain files, so `client-overrides/` and `server-overrides/` from the mrpack are not published (the converter warns). Only `overrides/` is, to both sides. The pack currently has none.
- Server-side configs are overwritten on update, same as the client.
