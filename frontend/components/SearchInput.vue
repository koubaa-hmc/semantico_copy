<script lang="ts" setup>
import IPButton from "~/components/IPButton.vue";

defineProps({
  modelValue: {
    type: String,
    required: false,
    default: "",
  },
  small: {
    type: Boolean,
    required: false,
    default: false,
  },
});

const emit = defineEmits(["update:modelValue", "click"]);
const inputRef = ref<HTMLInputElement | null>(null);

const updateSearchInput = (searchText: string) => {
  emit("update:modelValue", searchText);
};
const handleBtnClick = () => {
  emit("click");
};

const focus = () => {
  inputRef.value!.focus();
};

defineExpose({ focus });
</script>

<template>
  <form
    @click.stop.prevent
    @keyup.enter.prevent.stop
    @keydown.enter.prevent.stop
  >
    <label for="searchInput" class="mb-2 text-hmc-black sr-only">{{
      $t("btn_txt_search")
    }}</label>
    <div class="relative">
      <div
        v-if="!small"
        :title="$t('btn_txt_search')"
        class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
      >
        <img
          alt="magnifier icon"
          src="~/assets/images/magnifier-icon.svg"
          aria-hidden="true"
          class="w-5 h-5 text-gray-500 dark:text-gray-400"
        />
      </div>
      <input
        id="searchInput"
        ref="inputRef"
        :value="modelValue"
        :class="{ 'p-2': small, 'p-4 pl-10': !small }"
        type="search"
        class="block w-full text-hmc-black border border-gray-300 rounded-lg bg-white focus:ring-hmc-blue-light focus:border-blue-light"
        placeholder="Search"
        required
        @input="updateSearchInput(($event.target as HTMLInputElement).value)"
        @keyup.enter.stop.prevent="handleBtnClick"
      />
      <div
        v-if="small"
        class="absolute right-2.5 bottom-2.5 cursor-pointer"
        @click.prevent.stop="handleBtnClick"
      >
        <img
          alt="magnifier icon"
          src="~/assets/images/magnifier-icon.svg"
          aria-hidden="true"
          class="w-5 h-5 text-gray-500 dark:text-gray-400"
        />
      </div>
      <IPButton
        v-else
        secondary
        class="absolute right-2.5 bottom-2.5"
        @click.prevent.stop="handleBtnClick"
      >
        {{ $t("btn_txt_search") }}
      </IPButton>
    </div>
  </form>
</template>
