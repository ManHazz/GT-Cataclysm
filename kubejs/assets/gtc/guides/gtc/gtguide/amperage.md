---
navigation:
  title: "Amperage and Overload"
  icon: gtceu:lv_energy_input_hatch
  parent: power.md
  position: 60
item_ids:
  - gtceu:lv_energy_input_hatch
  - gtceu:tin_single_cable
---

# Amperage and Overload

<ItemImage id="gtceu:lv_energy_input_hatch" scale="4" />

What makes machines stall, cables burn and hatches explode.

## What it does

Machines: a machine that receives an amp of power from a voltage above its tier explodes. A machine that runs out of power mid-recipe powerstalls: it stops, resets its recipe progress to 0, and waits to refill its buffer without deleting its items. A single-block machine buffers voltage x 64 EU, accepts 1 amp, and accepts 1 more when below 50% buffer while running (docs). Multiblocks run at the combined input of their energy hatches; a standard energy hatch accepts 2 amps and explodes if it receives an amp of too high a voltage (docs).

## How to make it

<RecipeFor id="gtceu:lv_energy_input_hatch" />

## What it makes and uses

Cables: too much voltage destroys the cable but protects the machines behind it (the cable acts as a fuse). Too many amps heat it until it burns (docs).

Overclocking: a machine of a higher tier running a lower-tier recipe overclocks. The docs rule is 4x EU/t for half the time, so total energy rises 2x per overclock tier.

<ItemGrid>
  <ItemIcon id="gtceu:lv_energy_input_hatch" />
  <ItemIcon id="gtceu:tin_single_cable" />
  <ItemIcon id="gtceu:lv_battery_buffer_4x" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/power_line.nbt" />
  <BlockAnnotation x="0" y="0" z="1">Generator: 1 amp at its own voltage.</BlockAnnotation>
  <BlockAnnotation x="3" y="0" z="1">Transformer: changes voltage and amperage together.</BlockAnnotation>
  <BlockAnnotation x="6" y="0" z="1">Machine: explodes if fed above its tier.</BlockAnnotation>
</GameScene>

## Tips

* Safest rule from the docs: never run cables that carry fewer amps than the generators or buffers feeding them can supply.
* Large boilers also explode if given fuel but no water (tooltip). See [Large Boilers](large_boilers.md).
* A Soft Mallet right-click puts a powerstalling machine on standby without deleting its items (docs).
