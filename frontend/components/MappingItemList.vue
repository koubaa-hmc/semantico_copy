<script lang="ts" setup>
import type { PropType } from "vue";
import type { IPBaseObject } from "~/utils/types/CommonProperties";
import BorderBox from "~/components/BorderBox.vue";
import ExternalLink from "~/components/ExternalLink.vue";
import InternalLink from "~/components/InternalLink.vue";

defineProps({
  categoryList: {
    type: Array as PropType<IPBaseObject[]>,
    required: true,
  },
});
</script>

<template>
  <BorderBox>
    <table class="w-full table-fixed break-words">
      <thead class="text-xl font-black">
        <tr class="border-b-2 border-black">
          <td>Name</td>
          <td class="w-1/3">
            Keywords
          </td>
        </tr>
      </thead>
      <tbody class="text-base align-top">
        <tr
          v-for="listItem in categoryList"
          :key="listItem._id"
          class="border-b"
        >
          <td class="pr-5 pt-2">
            <div v-if="listItem.resourceUri">
              <ExternalLink :href="listItem.resourceUri[0]">
                {{ listItem.resourceName[0].name }}
              </ExternalLink>
              <InternalLink
                class="mx-4 text-sm"
                :to="'../MappingItem/' + listItem._id"
              >
                Details
              </InternalLink>
            </div>
            <div v-else>
              {{ listItem.resourceName[0].name }}
              <InternalLink
                class="mx-4 text-sm"
                :to="'../MappingItem/' + listItem._id"
              >
                Details
              </InternalLink>
            </div>
            <div v-if="listItem.resourceDescription" class="text-sm pb-2">
              {{ listItem.resourceDescription }}
            </div>
          </td>
          <td class="pt-2">
            {{ listItem.keyword?.join() }}
          </td>
        </tr>
      </tbody>
    </table>
  </BorderBox>
</template>
