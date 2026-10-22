---
navigation:
  title: "Batteries and Buffers"
  icon: gtceu:lv_battery_buffer_4x
  parent: power.md
  position: 50
item_ids:
  - gtceu:lv_battery_buffer_4x
  - gtceu:lv_battery_buffer_8x
  - gtceu:lv_battery_buffer_16x
---

# Batteries and Buffers

<ItemImage id="gtceu:lv_battery_buffer_4x" scale="4" />

A Battery Buffer holds batteries, smooths out power and hands out several amps from a single block.

## What it does

A Battery Buffer has 1, 4, 8 or 16 battery slots. It accepts 2 amps per contained electric item and outputs 1 amp per contained battery, charging and discharging all batteries evenly (docs). It is the main bulk storage from LV to mid EV.

## How to make it

<RecipeFor id="gtceu:lv_battery_buffer_4x" />

## What it makes and uses

<ItemGrid>
  <ItemIcon id="gtceu:lv_battery_buffer_4x" />
  <ItemIcon id="gtceu:lv_battery_buffer_8x" />
  <ItemIcon id="gtceu:lv_battery_buffer_16x" />
</ItemGrid>

Batteries are normally made in the Canner from a battery hull plus dust such as lithium, cadmium or sodium (docs). A battery in a machine's own battery slot charges when the machine's buffer is more than 2/3 full and discharges when it is under 1/3 (docs).

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_battery_buffer_4x" />
  <BlockAnnotation x="0" y="0" z="0">Cables in on any non-output side, up to 4 amps out of the output side with four batteries.</BlockAnnotation>
</GameScene>

## Tips

* The docs recommend your first EBF is fed by four LV generators or a 4x Battery Buffer.
* Never run a cable that carries fewer amps than the buffer can output (docs).
