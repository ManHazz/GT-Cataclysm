---
navigation:
  title: "LV Centrifuge"
  icon: gtceu:lv_centrifuge
  parent: machines.md
  position: 100
item_ids:
  - gtceu:lv_centrifuge
---

# LV Centrifuge

<ItemImage id="gtceu:lv_centrifuge" scale="4" />

The Centrifuge separates mixtures and compounds into their parts.

## What it does

Spins dusts apart and splits mixtures. Chances in brackets are byproduct chances (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_centrifuge" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Centrifuge | Ash Dust (any) | Quicklime Dust (49.5%), Potash Dust (16%), Magnesia Dust (15%), Phosphorus Pentoxide Dust (0.6%), Soda Ash Dust (6%), Hematite Dust (2.75%) | 30 | 12 s |
| Centrifuge | 4x Bronze Dust (any) | Tin Dust, 3x Copper Dust | 30 | 22.8 s |
| Centrifuge | Iron Pure Dust (any) | Iron Dust, Tin Dust (11.11%) | 5 | 5 s |

<ItemGrid>
  <ItemIcon id="gtceu:ash_dust" />
  <ItemIcon id="gtceu:bronze_dust" />
  <ItemIcon id="gtceu:tin_dust" />
  <ItemIcon id="gtceu:copper_dust" />
  <ItemIcon id="gtceu:iron_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_centrifuge" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* Bronze dust can be split back into tin and copper dust.
