<script lang="ts" setup>
import { navigateTo } from "#imports";
import { MappingCategory } from "~/utils/types/MappingCategory";
import NoScriptMessage from "~/components/NoScriptMessage.vue";
import BorderBox from "~/components/BorderBox.vue";
import IPButton from "~/components/IPButton.vue";

const localePath = useLocalePath();
</script>

<template>
  <NuxtLayout name="main">
    <NuxtLoadingIndicator :height="5" />
    <h1 class="text-4xl font-bold">
      {{ $t("information_portal_name") }}
    </h1>
    <NoScriptMessage />
    <BorderBox>
      {{ $t("intro_text") }}
    </BorderBox>
    <BorderBox class="grid grid-cols-4 gap-8">
      <IPButton
        v-for="(value, key) in MappingCategory"
        :key="value"
        secondary
        @click="navigateTo(localePath('/MappingItemList/' + key))"
      >
        {{ key }}
      </IPButton>
    </BorderBox>
  </NuxtLayout>
</template>
