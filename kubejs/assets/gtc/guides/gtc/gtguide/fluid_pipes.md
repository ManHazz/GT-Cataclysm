---
navigation:
  title: "Fluid Pipes"
  icon: gtceu:bronze_normal_fluid_pipe
  parent: steam.md
  position: 40
item_ids:
  - gtceu:bronze_normal_fluid_pipe
---

# Fluid Pipes

<ItemImage id="gtceu:bronze_normal_fluid_pipe" scale="4" />

Fluid pipes carry steam, water and every other fluid between machines.

## What it does

Each pipe block is a small tank. Pipes also have a maximum temperature and a list of fluid types they can safely contain (docs and tooltips). Pipes come in Tiny (fluid only), Small, Normal, Large and Huge sizes.

## How to make it

<RecipeFor id="gtceu:bronze_normal_fluid_pipe" />

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Extruder | 3x Bronze Ingot (any), Normal Pipe Extruder Mold (not consumed) | Bronze Normal Fluid Pipe | 42 | 11.4 s |

## What it makes and uses

| Pipe material | Max temperature | Gas | Acid | Cryogenic | Plasma |
|---|---|---|---|---|---|
| Wood | 340 K | no | no | no | no |
| Treated Wood | 340 K | no | no | no | no |
| Bronze | 1696 K | yes | no | no | no |
| Steel | 1855 K | yes | no | no | no |
| Stainless Steel | 2428 K | yes | yes | yes | no |
| Titanium | 2426 K | yes | no | no | no |
| Polytetrafluoroethylene | 600 K | yes | yes | no | no |

Fluid containment hazards (docs): too-hot fluids destroy the pipe, acids and cryogenics hurt their surroundings and then explode, and gases that cannot be contained escape and cause small explosions.

## How it connects

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="structures/steam_setup.nbt" />
  <BlockAnnotation x="1" y="0" z="1">Bronze Normal Fluid Pipe</BlockAnnotation>
  <BlockAnnotation x="3" y="0" z="1">Pipes connect to adjacent machines and pipes.</BlockAnnotation>
</GameScene>

## Tips

* Placement (docs): a pipe placed normally does not connect to anything; shift-right-click it against a machine or pipe to place it connected.
* Wrench a pipe to connect or disconnect a side. Shift-wrench a side to make it output-only.
* Fluids above 320 K or below 260 K in a pipe injure entities that touch it (docs).
