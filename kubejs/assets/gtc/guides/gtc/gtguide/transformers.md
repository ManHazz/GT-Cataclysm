---
navigation:
  title: "Transformers and Diodes"
  icon: gtceu:lv_transformer_1a
  parent: power.md
  position: 40
item_ids:
  - gtceu:lv_transformer_1a
  - gtceu:lv_transformer_2a
  - gtceu:lv_transformer_4a
  - gtceu:lv_transformer_16a
  - gtceu:lv_diode
---

# Transformers and Diodes

<ItemImage id="gtceu:lv_transformer_1a" scale="4" />

Transformers step power between two neighbouring tiers. Diodes make power flow one way and cap its amperage.

## What it does

A transformer turns 1 amp of the higher tier into 4 amps of the lower tier, or the reverse. The docs example: an LV Transformer accepts 1A MV and emits 4A LV, or accepts 4A LV and emits 1A MV. The Hi-Amp variants convert 2A to 8A and 4A to 16A, and the Power Transformer converts 16A to 64A.

## How to make it

<RecipeFor id="gtceu:lv_transformer_1a" />

<RecipeFor id="gtceu:lv_diode" />

## What it makes and uses

A new transformer starts in Transform Down mode. The in-game tooltip says to use a Screwdriver to change the mode (the online docs say Soft Mallet; trust the tooltip in your game). A Diode starts at 1A; the tooltip says use a Soft Mallet to cycle its amperage.

<ItemGrid>
  <ItemIcon id="gtceu:lv_transformer_1a" />
  <ItemIcon id="gtceu:lv_transformer_2a" />
  <ItemIcon id="gtceu:lv_transformer_4a" />
  <ItemIcon id="gtceu:lv_transformer_16a" />
  <ItemIcon id="gtceu:lv_diode" />
</ItemGrid>

Diodes can sit in the walls of a Cleanroom to bring power in (docs).

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/power_line.nbt" />
  <BlockAnnotation x="3" y="0" z="1">LV Transformer in Transform Down mode: 1A MV in, 4A LV out.</BlockAnnotation>
</GameScene>

## Tips

* Transformers let a few high-voltage generators feed many low-voltage machines (docs).
* Diodes accept amps equal to their output setting and re-emit them at full voltage, which also helps against cable loss (docs).
