# Changelog

## 0.3.1 - 2026-10-20

### Fixed
- GregTech machine recipes in JEI show item tooltips again (JEI pinned to 15.49.0.200; newer JEI broke GTCEu/LDLib slot tooltips).
- Polymorph pinned to 0.49.10 for compatibility with JEI 15.49.0.200.
- JEI config moved to the correct path (config/jei/client/).

## 0.3.0 - 2026-10-20

Upgrading: re-import the 0.3.0 mrpack once, then set up auto-update (see docs/AUTO_UPDATE.md).

### Added
- GuideME GregTech visual guide: 44 pages, 9 3D structures. Hold G on items to open.
- Ponder scenes via PonderJS (hold W): LV macerator, EBF, steam setup, power line, cleanroom, ore line.
- Automatic updates via packwiz-installer.
- CI headless client test.

### Changed
- JEI tag-content grid hidden; Tooltip Scaler added.
- Tooltips wrapped and extended.
- G key conflicts moved: Curios to `;`, jetpack to `[`.

## 0.2.2 - 2026-10-20

### Fixed
- Field guide "Loading error!": all entry categories are now fully qualified (patchouli:<category>).
- Disabled the Heracles "Discover Quests!" toast (heracles_options.json, showTutorial=false).

## 0.2.1 - 2026-10-20

Clients must re-import the 0.2.1 mrpack.

### Added
- Patchouli GregTech Field Guide with a Pokedex-style Boss Index.
- Players receive the field guide on first login.
- New tooltips for machine hulls, boss drops, eyes, and the Quest Book.

### Changed
- Tooltips are wrapped at 40 characters.
- Welcome and Bosses quests now mention the field guide.

## 0.2.0 - 2026-10-13

### Added
- QoL mods: Mouse Tweaks, Enchantment Descriptions, Toast Control, Chat Heads, Better Advancements, Default Options (with Open Quests bound to J), AppleSkin, Just Enough Resources, Polymorph, Corpse, Open Parties and Claims, Crafting Tweaks.
- FallingTree for tree felling.
- Controlling + Searchables for a readable Key Binds screen.
- Players receive a Quest Book on first join.

### Changed
- Vanilla ores are enabled alongside GT veins.
- Quest chapter names shortened so the sidebar fits.
- Machine hull recipes use GT fluid tags.

### Upgrading from 0.1.0
- A new world is required to get vanilla ores; existing worlds will not generate them in already-explored chunks.
- Clients must re-import the 0.2.0 mrpack.

## 0.1.0 - 2026-10-13

Initial pack.

- GTCEu 7.5.3 + L_Ender's Cataclysm 3.31.
- Boss-gated machine hulls (MV-ZPM) using boss items as non-consumed catalysts.
- Heracles questbook with 79 quests.
- Performance mods; Embeddium/Oculus with Potato and MakeUp shaders.
- Xaero's maps and AE2.
- CI: JSON/KubeJS validation and headless server boot.
