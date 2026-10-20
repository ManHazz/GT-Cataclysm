---
navigation:
  title: "Crushed Ore"
  icon: gtceu:crushed_iron_ore
  parent: ores.md
  position: 20
item_ids:
  - gtceu:crushed_iron_ore
  - gtceu:purified_iron_ore
  - gtceu:refined_iron_ore
---

# Crushed Ore

<ItemImage id="gtceu:crushed_iron_ore" scale="4" />

Crushed ore is the first product of ore processing and has three possible next steps.

## What it does

Crushed ore can be washed to purified ore, cooked in a Thermal Centrifuge to refined ore, or macerated to impure dust. Which you pick decides your byproducts.

## How to make it

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Macerator | Iron Ore | 2x Crushed Iron Ore, Nickel Dust (14%), Stone Dust (67%) | 2 | 20 s |
| Macerator | Iron Raw Ore (any) | 2x Crushed Iron Ore, Nickel Dust (14%) | 2 | 20 s |

Two ores per ore block or raw ore, from the table above.

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Ore Washer | Iron Crushed Ore (any), Programmed Circuit (config 1, not consumed), 1000 mB Water | Purified Iron Ore, Nickel Dust (33.33%), Stone Dust | 16 | 20 s |
| Thermal Centrifuge | Iron Crushed Ore (any) | Refined Iron Ore, Tin Dust (33.33%), Stone Dust | 30 | 20 s |
| Macerator | Iron Crushed Ore (any) | Impure Iron Dust, Nickel Dust (14%) | 2 | 20 s |

<ItemGrid>
  <ItemIcon id="gtceu:crushed_iron_ore" />
  <ItemIcon id="gtceu:purified_iron_ore" />
  <ItemIcon id="gtceu:refined_iron_ore" />
  <ItemIcon id="gtceu:impure_iron_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <Block id="gtceu:lv_ore_washer" x="0" y="0" z="0" />
  <BlockAnnotation x="0" y="0" z="0">Wash: purified ore</BlockAnnotation>
  <Block id="gtceu:lv_thermal_centrifuge" x="2" y="0" z="0" />
  <BlockAnnotation x="2" y="0" z="0">Thermal centrifuge: refined ore</BlockAnnotation>
  <Block id="gtceu:lv_macerator" x="4" y="0" z="0" />
  <BlockAnnotation x="4" y="0" z="0">Macerate: impure dust</BlockAnnotation>
</GameScene>

## Tips

* See [The Ore Chain](ore_chain.md) for the full route.
