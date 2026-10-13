// Give every player one Heracles Quest Book on first login (the Open Quests key defaults to U, which clashes with JEI/Xaero).
PlayerEvents.loggedIn(event => {
  const player = event.player;
  if (player.persistentData.getBoolean('gtc_got_quest_book')) return;
  player.give('heracles:quest_book');
  player.persistentData.putBoolean('gtc_got_quest_book', true);
});
