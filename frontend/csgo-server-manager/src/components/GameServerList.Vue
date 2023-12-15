<template lang="">
  <div>
    <game-servers-list :game-servers="gameServers"></game-servers-list>
    <add-server @add-server="addServer"></add-server>
  </div>
</template>
<script>
setup() {
  const gameServers = ref([
    {
      name: "server 1"
    },
    {
      name: "server 2"
    }
  ]);

  function addServer (name) {
    const newServer = {
      id: new Date().toISOString(),
      name: name
    },
    gameServers.value.push(newServer);
  }

  return {
    gameServers: gameServers,
  };
}
</script>
<style lang=""></style>
