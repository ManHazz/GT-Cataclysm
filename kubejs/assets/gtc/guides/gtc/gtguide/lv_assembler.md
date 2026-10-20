---
navigation:
  title: "LV Assembler"
  icon: gtceu:lv_assembler
  parent: machines.md
  position: 70
item_ids:
  - gtceu:lv_assembler
---

# LV Assembler

<ItemImage id="gtceu:lv_assembler" scale="4" />

The Assembler combines several items, and sometimes a fluid, into one product.

## What it does

It builds pistons, inductors, casings and machine hulls (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_assembler" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Assembler | Steel Plate (any), 3x Planks (any), 4x Stone Crafting Materials (any), Redstone Dust (any) | 2x Piston | 16 | 5 s |
| Assembler | Steel Ring (any), 2x Copper Fine Wire (any), 36 mB Polyethylene | 2x Inductor | 120 | 16 s |
| Assembler | 8x Steel Plate (any), Programmed Circuit (config 8, not consumed) | LV Machine Casing | 16 | 2.5 s |
| Assembler | LV Machine Casing, 2x Tin Single Cable, 288 mB Polyethylene | LV Machine Hull | 16 | 2.5 s |

<ItemGrid>
  <ItemIcon id="minecraft:piston" />
  <ItemIcon id="gtceu:inductor" />
  <ItemIcon id="gtceu:lv_machine_casing" />
  <ItemIcon id="gtceu:lv_machine_hull" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_assembler" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* MV and higher hulls have their assembler recipes replaced in this pack: see [Pack: boss-gated hulls](pack.md).
* The Assembly Line is a different machine, not a bigger Assembler (tooltip): see [Assembly Line](assembly_line.md).
