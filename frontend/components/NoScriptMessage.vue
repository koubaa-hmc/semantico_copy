<script lang="ts" setup>
import BorderBox from "~/components/BorderBox.vue";
</script>

<template>
  <component :is="'noscript'">
    <BorderBox warning>
      {{ $t("no_javascript_message") }}
    </BorderBox>
  </component>
</template>
