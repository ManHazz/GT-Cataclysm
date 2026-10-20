---
navigation:
  title: "LV Macerator"
  icon: gtceu:lv_macerator
  parent: machines.md
  position: 10
item_ids:
  - gtceu:lv_macerator
  - gtceu:mv_macerator
---

# LV Macerator

<ItemImage id="gtceu:lv_macerator" scale="4" />

The Macerator crushes ores into crushed ore, which doubles your yield. It runs on LV power (up to 32 V).

## What it does

One ore becomes two crushed ore (see the first row below). Tooltips: the LV and MV Macerators work without byproducts; the HV Macerator tooltip says it works with byproducts, so the byproduct chances in the table apply from HV up.

Available in these tiers: steam (low and high pressure), LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_macerator" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Macerator | Iron Ore | 2x Crushed Iron Ore, Nickel Dust (14%), Stone Dust (67%) | 2 | 20 s |
| Macerator | Iron Raw Ore (any) | 2x Crushed Iron Ore, Nickel Dust (14%) | 2 | 20 s |
| Macerator | Iron Crushed Ore (any) | Impure Iron Dust, Nickel Dust (14%) | 2 | 20 s |
| Macerator | Iron Purified Ore (any) | Pure Iron Dust, Tin Dust (14%) | 2 | 20 s |
| Macerator | Iron Refined Ore (any) | Iron Dust, Tin Dust (14%) | 2 | 20 s |

<ItemGrid>
  <ItemIcon id="gtceu:iron_ore" />
  <ItemIcon id="gtceu:copper_ore" />
  <ItemIcon id="minecraft:raw_iron" />
  <ItemIcon id="minecraft:raw_copper" />
  <ItemIcon id="gtceu:crushed_iron_ore" />
  <ItemIcon id="gtceu:impure_iron_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_macerator" />
  <BlockAnnotation x="0" y="0" z="0">Insert ore, supply LV power.</BlockAnnotation>
</GameScene>

## Tips

* Raw iron and raw copper are macerated through the tags forge:raw_materials/iron and forge:raw_materials/copper (confirmed in game).
* The steam version is on [Steam Macerator](steam_macerator.md). The whole chain is on [Ore processing](ores.md).
