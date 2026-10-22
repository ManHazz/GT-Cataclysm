---
navigation:
  title: "LV Compressor"
  icon: gtceu:lv_compressor
  parent: machines.md
  position: 30
item_ids:
  - gtceu:lv_compressor
---

# LV Compressor

<ItemImage id="gtceu:lv_compressor" scale="4" />

The Compressor squeezes items into denser forms.

## What it does

Packs nuggets into ingots and ingots into blocks, among other things (recipes below).

Available in these tiers: steam (low and high pressure), LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_compressor" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Compressor | 9x Red Alloy Ingot (any) | Red Alloy Block | 2 | 15 s |
| Compressor | 9x Iron Nugget (any) | Iron Ingot | 2 | 15 s |
| Compressor | 8x Wheat | Plant Ball | 2 | 15 s |

<ItemGrid>
  <ItemIcon id="gtceu:red_alloy_ingot" />
  <ItemIcon id="gtceu:red_alloy_block" />
  <ItemIcon id="minecraft:iron_nugget" />
  <ItemIcon id="minecraft:iron_ingot" />
  <ItemIcon id="gtceu:plant_ball" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_compressor" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* The Compressor also makes Plant Balls from wheat, a fuel for boilers (it appears in the steam boiler fuel list).
