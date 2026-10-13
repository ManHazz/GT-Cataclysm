# GT-Cataclysm

[![CI](https://github.com/ManHazz/GT-Cataclysm/actions/workflows/ci.yml/badge.svg)](https://github.com/ManHazz/GT-Cataclysm/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/ManHazz/GT-Cataclysm)](https://github.com/ManHazz/GT-Cataclysm/releases)
![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1-62B47A)
![Forge](https://img.shields.io/badge/Forge-47.4.13-DFA86A)
![GregTech CEu Modern](https://img.shields.io/badge/GregTech%20CEu%20Modern-7.5.3-blue)
![L_Ender's Cataclysm](https://img.shields.io/badge/L__Ender's%20Cataclysm-3.31-red)
![Java](https://img.shields.io/badge/Java-17-orange)

## About

A Minecraft 1.20.1 Forge modpack where GregTech progression is gated by L_Ender's Cataclysm bosses. Performance-first, with lightweight shaders, AE2, Xaero's map, and no Create.

## Download

Get the latest `.mrpack` (client) and server pack from the [Releases page](https://github.com/ManHazz/GT-Cataclysm/releases).

## Status

Pre-alpha: planning stage. See [PLAN.md](PLAN.md).

## Building

Managed with [Pakku](https://github.com/juraj-hrivnak/Pakku):

```sh
java -jar pakku.jar fetch
java -jar pakku.jar export
```

## Recommended JVM args

Java 17, G1GC, 6-8 GB of RAM:

```
-Xms6G -Xmx8G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15
```

## Contributing / CI

Every push and PR to `main` runs CI: `validate` (JSON parsing, KubeJS syntax, required docs) and `server-boot` (fetches the pack, installs Forge, and boots a headless server until `Done (`).
