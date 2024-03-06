<script lang="ts" setup>
import JsonObj from "~/components/json/JsonObj.vue";
import JsonArray from "~/components/json/JsonArray.vue";

const props = defineProps<{
  json: any;
}>();

function dataTypeOf(json: any) {
  // taken from https://stackoverflow.com/a/8511350
  if (typeof json === "object" && !Array.isArray(json) && json !== null) {
    return "object";
  }
  if (Array.isArray(json)) {
    return "array";
  }
  if (typeof json === "undefined") {
    return "undefined";
  }
  if (typeof json === "boolean") {
    return "boolean";
  }
  if (typeof json === "number") {
    return "number";
  }
  if (typeof json === "string") {
    return "string";
  }
  if (json === null) {
    return "null";
  }
  return "other";
}
</script>

<template>
  <div>
    <JsonObj v-if="dataTypeOf(props.json) === 'object'" :obj="props.json" />
    <JsonArray
      v-else-if="dataTypeOf(props.json) === 'array'"
      :array="props.json"
    />
    <div v-else>
      {{ props.json }}
    </div>
  </div>
</template>
