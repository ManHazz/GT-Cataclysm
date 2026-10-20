---
navigation:
  title: "LV Electrolyzer"
  icon: gtceu:lv_electrolyzer
  parent: machines.md
  position: 110
item_ids:
  - gtceu:lv_electrolyzer
---

# LV Electrolyzer

<ItemImage id="gtceu:lv_electrolyzer" scale="4" />

The Electrolyzer splits compounds into elements with electricity.

## What it does

Breaks dusts and fluids apart (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_electrolyzer" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Electrolyzer | 1000 mB Salt Water | 3x Sodium Hydroxide Dust, 1000 mB Chlorine, 1000 mB Hydrogen | 30 | 36 s |
| Electrolyzer | 2x Sphalerite Dust (any) | Zinc Dust, Sulfur Dust, Gallium Dust (7.5%) | 30 | 10 s |
| Electrolyzer | 13x Clay Dust (any) | 2x Sodium Dust, Lithium Dust, 2x Aluminium Dust, 2x Silicon Dust, 6000 mB Water | 60 | 9.1 s |

<ItemGrid>
  <ItemIcon id="gtceu:sodium_hydroxide_dust" />
  <ItemIcon id="gtceu:zinc_dust" />
  <ItemIcon id="gtceu:sulfur_dust" />
  <ItemIcon id="gtceu:aluminium_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_electrolyzer" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* The Large Electrolysis Chamber is the multiblock version (item gtceu:large_electrolyzer).
