<script lang="ts" setup>
defineProps({
  warning: {
    type: Boolean,
    required: false,
    default: false,
  },
});
</script>

<template>
  <div :class="[warning ? 'border-red-600' : '']" class="border-2 p-4 my-4">
    <slot />
  </div>
</template>
