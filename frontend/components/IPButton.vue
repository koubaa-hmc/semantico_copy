<script lang="ts" setup>
const props = defineProps({
  secondary: {
    type: Boolean,
    required: false,
    default: false,
  },
  disabled: {
    type: Boolean,
    required: false,
    default: false,
  },
});

const classes = computed(() => {
  if (!props.secondary && !props.disabled) {
    return "bg-hmc-green hover:bg-hmc-blue-dark";
  } else if (props.secondary && !props.disabled) {
    return "bg-hmc-blue-dark hover:bg-hmc-blue";
  } else {
    return "bg-gray-400 pointer-none cursor-default";
  }
});
</script>

<template>
  <button
    :class="classes"
    class="rounded-lg text-md text-white px-4 py-2 font-medium focus:ring-4 focus:outline-none focus:ring-hmc-blue-light"
  >
    <slot />
  </button>
</template>
