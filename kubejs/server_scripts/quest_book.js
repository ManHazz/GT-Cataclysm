// Give every player one Heracles Quest Book on first login (the Open Quests key defaults to U, which clashes with JEI/Xaero).
PlayerEvents.loggedIn(event => {
  const player = event.player;
  if (player.persistentData.getBoolean('gtc_got_quest_book')) return;
  player.give('heracles:quest_book');
  player.persistentData.putBoolean('gtc_got_quest_book', true);
});

// Give every player one GregTech Field Guide (Patchouli external book patchouli:gtc_guide) once; separate flag so existing players get it too.
PlayerEvents.loggedIn(event => {
  const player = event.player;
  if (player.persistentData.getBoolean('gtc_got_guide_book')) return;
  player.give(Item.of('patchouli:guide_book', '{"patchouli:book":"patchouli:gtc_guide"}'));
  player.persistentData.putBoolean('gtc_got_guide_book', true);
});
