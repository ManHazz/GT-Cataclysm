---
navigation:
  title: "Cables"
  icon: gtceu:tin_single_cable
  parent: power.md
  position: 30
item_ids:
  - gtceu:tin_single_cable
  - gtceu:copper_single_cable
  - gtceu:tin_quadruple_cable
---

# Cables

<ItemImage id="gtceu:tin_single_cable" scale="4" />

Cables carry EU between generators, storage and machines. Every cable has a maximum voltage, a maximum amperage and a per-block loss.

## What it does

Cables connect on any side (toggle sides with Wire Cutters). A cable that carries too high a voltage burns up; one that carries too many amps heats up, loses its insulation and eventually burns (docs). Each block of cable an amp passes through loses some voltage. Wires can be combined into 2x, 4x, 8x and 16x versions to add up their amperage.

## How to make it

<RecipeFor id="gtceu:tin_single_cable" />

Higher-tier cables are insulated with an Assembler and liquid rubber; EV and above add thin PVC sheets (docs).

## What it makes and uses

| Cable material | Max voltage | Max amps (1x cable) | Loss per block per amp |
|---|---|---|---|
| Lead | 8 (ULV) | 2 | 2 |
| Tin | 32 (LV) | 1 | 1 |
| Copper | 128 (MV) | 1 | 2 |
| Annealed Copper | 128 (MV) | 1 | 1 |
| Gold | 512 (HV) | 3 | 2 |
| Aluminium | 2048 (EV) | 1 | 1 |
| Platinum | 8192 (IV) | 2 | 1 |

Superconductor wires have zero loss and need no insulation (docs). Example from the game data: Magnesium Diboride is a superconductor at 128 V with 0 loss.

<ItemGrid>
  <ItemIcon id="gtceu:tin_single_cable" />
  <ItemIcon id="gtceu:tin_double_cable" />
  <ItemIcon id="gtceu:tin_quadruple_cable" />
  <ItemIcon id="gtceu:tin_octal_cable" />
  <ItemIcon id="gtceu:tin_hex_cable" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/power_line.nbt" />
  <BlockAnnotation x="1" y="0" z="1">Copper cable (MV, 128 V)</BlockAnnotation>
  <BlockAnnotation x="4" y="0" z="1">Quadruple tin cable (LV, 32 V, 4 amps)</BlockAnnotation>
</GameScene>

## Tips

* Docs example: 16A of LV sent 20 blocks down 16x tin cable arrives at 12 V (68.75% of the power lost). The same power stepped up to MV, sent 20 blocks down 4x annealed copper cable and stepped back down loses 15.6%.
* Loss is subtracted per amp, not multiplied, so few high-voltage amps travel farther than many low-voltage amps (docs).
* Never touch an uninsulated wire that carried energy: it damages you (docs).
