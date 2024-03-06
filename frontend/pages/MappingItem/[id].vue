<script lang="ts" setup>
import BorderBox from "~/components/BorderBox.vue";
import { useRoute, getItem } from "#imports";
import JsonBase from "~/components/json/JsonBase.vue";

const route = useRoute();

// Get the resource
const { data, pending, error } = await getItem(route.params.id.toString());
if (error && error.value) {
  console.error("Could not load resource " + route.params.id, error);
  // TODO handle this error more meaningfully
}
</script>

<template>
  <NuxtLayout name="main">
    <BorderBox>
      <div v-if="pending">
        {{ $t("loading_notice") }}
      </div>
      <div v-else-if="error">
        {{ $t("resource_unloadable_notice") }}
      </div>
      <div v-else>
        <dl class="divide-y">
          <div
            v-for="(value, key, index) in data"
            :key="index"
            class="py-3 first:pt-0"
          >
            <dt class="font-bold">
              {{ $t(key) }}
            </dt>
            <dd class="pl-7">
              <JsonBase :json="value" />
            </dd>
          </div>
        </dl>
      </div>
    </BorderBox>
  </NuxtLayout>
</template>
