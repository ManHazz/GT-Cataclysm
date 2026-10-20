---
navigation:
  title: "LV Electric Furnace"
  icon: gtceu:lv_electric_furnace
  parent: machines.md
  position: 20
item_ids:
  - gtceu:lv_electric_furnace
---

# LV Electric Furnace

<ItemImage id="gtceu:lv_electric_furnace" scale="4" />

The Electric Furnace smelts with EU instead of fuel.

## What it does

Runs furnace-style smelting. The steam Furnace uses the same recipe type, and the docs give its example as Bronze Dust to Bronze Ingot.

Available in these tiers: steam (low and high pressure), LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_electric_furnace" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Furnace | Bronze Dust (any) | Bronze Ingot | - | - |
| Furnace | Wrought Iron Dust (any) | Wrought Iron Ingot | - | - |

<ItemGrid>
  <ItemIcon id="gtceu:bronze_dust" />
  <ItemIcon id="gtceu:bronze_ingot" />
  <ItemIcon id="gtceu:wrought_iron_dust" />
  <ItemIcon id="gtceu:wrought_iron_ingot" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_electric_furnace" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* Alloys that need more heat are made in the [Electric Blast Furnace](ebf.md).
* The table shows furnace recipes added by GTCEu (recipe ids start with gtceu:smelting/); EU/t and time are not part of those recipes.
