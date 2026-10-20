---
navigation:
  title: "LV Extractor"
  icon: gtceu:lv_extractor
  parent: machines.md
  position: 40
item_ids:
  - gtceu:lv_extractor
---

# LV Extractor

<ItemImage id="gtceu:lv_extractor" scale="4" />

The Extractor pulls fluids and dusts out of items.

## What it does

Melts ingots into fluid and presses resin into raw rubber (recipes below). The steam Extractor docs example: Rubber Log to Raw Rubber Pulp.

Available in these tiers: steam (low and high pressure), LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_extractor" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Extractor | Sticky Resin | 3x Raw Rubber Dust | 2 | 7.5 s |
| Extractor | Cupronickel Ingot (any) | 144 mB Cupronickel | 30 | 3 s |

<ItemGrid>
  <ItemIcon id="gtceu:sticky_resin" />
  <ItemIcon id="gtceu:raw_rubber_dust" />
  <ItemIcon id="gtceu:cupronickel_ingot" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_extractor" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* Rubber is the insulation for LV cables: see [Cables](cables.md).
