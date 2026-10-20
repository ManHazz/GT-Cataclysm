---
navigation:
  title: "LV Circuit Assembler"
  icon: gtceu:lv_circuit_assembler
  parent: machines.md
  position: 80
item_ids:
  - gtceu:lv_circuit_assembler
---

# LV Circuit Assembler

<ItemImage id="gtceu:lv_circuit_assembler" scale="4" />

The Circuit Assembler builds circuit boards, chips and circuits.

## What it does

Takes a board, components and wire plus a fluid (tin in these recipes) and outputs circuits (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_circuit_assembler" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Circuit Assembler | Resin Printed Circuit Board, 2x Resistors (any), 2x Red Alloy Single Wire, 2x Circuits ULV (any), 144 mB Tin | 2x Basic Electronic Circuit | 16 | 10 s |
| Circuit Assembler | Phenolic Printed Circuit Board, 2x Basic Electronic Circuit, 2x Diodes (any), 2x Copper Single Wire, 144 mB Tin | Good Electronic Circuit | 30 | 15 s |
| Circuit Assembler | Plastic Printed Circuit Board, Cpu Chip, 2x Resistors (any), 2x Capacitors (any), 2x Transistors (any), 2x Copper Fine Wire (any), 144 mB Tin | 3x Microchip Processor | 60 | 10 s |

<ItemGrid>
  <ItemIcon id="gtceu:basic_electronic_circuit" />
  <ItemIcon id="gtceu:good_electronic_circuit" />
  <ItemIcon id="gtceu:microchip_processor" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_circuit_assembler" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* The LV Circuit Assembler's own crafting recipe needs MV circuits (see the recipe above).
