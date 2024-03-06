<script lang="ts" setup>
import JsonBase from "~/components/json/JsonBase.vue";

const props = defineProps({
  array: {
    type: Array,
    required: true,
  },
});
</script>

<template>
  <ul class="flex flex-wrap divide-x gap-y-1">
    <li v-for="(item, index) in props.array" :key="index" class="w-fit px-2">
      <JsonBase :json="item" />
    </li>
  </ul>
</template>
