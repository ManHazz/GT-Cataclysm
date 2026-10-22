---
navigation:
  title: "LV Chemical Reactor"
  icon: gtceu:lv_chemical_reactor
  parent: machines.md
  position: 90
item_ids:
  - gtceu:lv_chemical_reactor
---

# LV Chemical Reactor

<ItemImage id="gtceu:lv_chemical_reactor" scale="4" />

The Chemical Reactor makes chemicals from items and fluids.

## What it does

Reacts dusts and fluids into new dusts and fluids (recipes below). Some recipes need a catalyst that is not consumed, such as silver dust.

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_chemical_reactor" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Chemical Reactor | 2x Quicklime Dust (any), 1000 mB Water | 3x Calcium Hydroxide Dust | 60 | 5 s |
| Chemical Reactor | 1000 mB Sulfur Dioxide, 1000 mB Oxygen | 1000 mB Sulfur Trioxide | 7 | 10 s |
| Chemical Reactor | Silver Dust (any) (not consumed), 1000 mB Methanol, 1000 mB Oxygen | 1000 mB Formaldehyde, 1000 mB Water | 480 | 5 s |

<ItemGrid>
  <ItemIcon id="gtceu:calcium_hydroxide_dust" />
  <ItemIcon id="gtceu:quicklime_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_chemical_reactor" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* The Large Chemical Reactor multiblock overclocks perfectly (4x EU/t for 1/4 the time, docs).
