<script lang="ts" setup>
import JsonBase from "~/components/json/JsonBase.vue";

const props = defineProps({
  obj: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <dl>
    <div v-for="(value, key, index) in props.obj" :key="index" class="pb-1">
      <dt class="font-bold">
        {{ $t(key) }}
      </dt>
      <dd class="pl-7">
        <JsonBase :json="value" />
      </dd>
    </div>
  </dl>
</template>
