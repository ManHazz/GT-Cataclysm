---
navigation:
  title: "The Ore Chain"
  icon: gtceu:iron_ore
  parent: ores.md
  position: 10
item_ids:
  - gtceu:iron_ore
  - gtceu:crushed_iron_ore
  - gtceu:purified_iron_ore
  - gtceu:refined_iron_ore
  - gtceu:impure_iron_dust
  - gtceu:pure_iron_dust
  - gtceu:iron_dust
---

# The Ore Chain

<ItemImage id="gtceu:iron_ore" scale="4" />

Ore does not go straight to a furnace in GregTech. Each stage gives a bit more output and extra byproducts. Iron is the worked example; the recipes are read from the game.

## What it does

Main path: Ore -> Macerator -> Crushed Ore -> Ore Washer -> Purified Ore -> Thermal Centrifuge -> Refined Ore -> Macerator -> Dust. You can skip stages: crushed ore can be macerated straight to impure dust, and purified ore to pure dust. Dust is then smelted or processed further.

## How to make it

Every stage is a single-block machine from LV up:

* <ItemLink id="gtceu:lv_macerator" />
* <ItemLink id="gtceu:lv_ore_washer" />
* <ItemLink id="gtceu:lv_thermal_centrifuge" />
* <ItemLink id="gtceu:lv_centrifuge" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Macerator | Iron Ore | 2x Crushed Iron Ore, Nickel Dust (14%), Stone Dust (67%) | 2 | 20 s |
| Ore Washer | Iron Crushed Ore (any), Programmed Circuit (config 1, not consumed), 1000 mB Water | Purified Iron Ore, Nickel Dust (33.33%), Stone Dust | 16 | 20 s |
| Thermal Centrifuge | Iron Purified Ore (any) | Refined Iron Ore, Tin Dust (33.33%) | 30 | 20 s |
| Macerator | Iron Refined Ore (any) | Iron Dust, Tin Dust (14%) | 2 | 20 s |

Shortcuts and cleanup:

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Macerator | Iron Crushed Ore (any) | Impure Iron Dust, Nickel Dust (14%) | 2 | 20 s |
| Ore Washer | Iron Impure Dust (any), Programmed Circuit (config 2, not consumed), 100 mB Water | Iron Dust | 4 | 0.4 s |
| Macerator | Iron Purified Ore (any) | Pure Iron Dust, Tin Dust (14%) | 2 | 20 s |
| Centrifuge | Iron Pure Dust (any) | Iron Dust, Tin Dust (11.11%) | 5 | 5 s |
| Centrifuge | Iron Impure Dust (any) | Iron Dust, Nickel Dust (11.11%) | 24 | 11.2 s |

<ItemGrid>
  <ItemIcon id="gtceu:iron_ore" />
  <ItemIcon id="gtceu:crushed_iron_ore" />
  <ItemIcon id="gtceu:purified_iron_ore" />
  <ItemIcon id="gtceu:refined_iron_ore" />
  <ItemIcon id="gtceu:impure_iron_dust" />
  <ItemIcon id="gtceu:pure_iron_dust" />
  <ItemIcon id="gtceu:iron_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <Block id="gtceu:lv_macerator" x="0" y="0" z="0" />
  <BlockAnnotation x="0" y="0" z="0">1. Macerator: ore to crushed ore</BlockAnnotation>
  <Block id="gtceu:lv_ore_washer" x="2" y="0" z="0" />
  <BlockAnnotation x="2" y="0" z="0">2. Ore Washer: crushed to purified ore (water)</BlockAnnotation>
  <Block id="gtceu:lv_thermal_centrifuge" x="4" y="0" z="0" />
  <BlockAnnotation x="4" y="0" z="0">3. Thermal Centrifuge: purified to refined ore</BlockAnnotation>
  <Block id="gtceu:lv_centrifuge" x="6" y="0" z="0" />
  <BlockAnnotation x="6" y="0" z="0">4. Centrifuge: cleans up dusts</BlockAnnotation>
</GameScene>

## Tips

* Percentages in the output column are byproduct chances. Each stage has different byproducts for the same ore.
* Machine tiers differ in how many output slots they have; see [LV Macerator](lv_macerator.md) for the byproduct note.
