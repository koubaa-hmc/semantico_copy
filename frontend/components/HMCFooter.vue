<script lang="ts" setup>
import ExternalLink from "~/components/ExternalLink.vue";
</script>

<template>
  <footer class="bg-hmc-blue-dark p-6 pb-5 text-white text-base leading-5">
    <div class="container mx-auto">
      <div class="flex flex-col">
        <div class="flex flex-wrap justify-between">
          <div>
            <ExternalLink :href="$t('helmholtz_url')">
              <img
                src="~/assets/images/Helmholtz_Logo.svg"
                alt="Helmholtz Logo"
                width="200"
                height="28"
              />
            </ExternalLink>
          </div>
          <div>
            {{ $t("helmholtz_slogan") }}
          </div>
        </div>
        <div class="flex flex-row mt-10 space-x-4 items-center">
          <ExternalLink :href="$t('hmc_public_mattermost_url')">
            <img
              src="~/assets/images/Mattermost_Logo.svg"
              alt="Mattermost Logo"
              width="23"
              height="23"
            />
          </ExternalLink>
          <ExternalLink
            :href="$t('hmc_mastodon_url')"
            aria-label="Mastodon Link"
          >
            <img
              src="~/assets/images/Mastodon_Logo.svg"
              alt="Mastodon Logo"
              width="23"
              height="23"
            />
          </ExternalLink>
          <ExternalLink
            :href="$t('hmc_linkedin_url')"
            aria-label="Linkedin Link"
          >
            <img
              src="~/assets/images/Linkedin_Logo.svg"
              alt="Linkedin Logo"
              width="22"
              height="22"
            />
          </ExternalLink>
          <ExternalLink :href="$t('hmc_twitter_url')">
            <img
              src="~/assets/images/Twitter_Logo.svg"
              alt="Twitter Logo"
              width="22"
              height="22"
            />
          </ExternalLink>
        </div>
        <div class="mt-7">
          {{ $t("hmc_information_portal_name") }}:
        </div>
        <div
          class="flex flex-col mt-1 gap-6 md:flex-row flex-wrap justify-between"
        >
          <div class="flex flex-row space-x-10 items-end">
            <ExternalLink secondary>
              {{ $t("lnk_txt_imprint") }}
            </ExternalLink>
            <ExternalLink secondary>
              {{ $t("lnk_txt_data_policy") }}
            </ExternalLink>
            <ExternalLink secondary :href="$t('contact_url')">
              {{ $t("lnk_txt_contact") }}
            </ExternalLink>
          </div>
          <div class="flex flex-col md:items-end">
            <div>
              &copy; {{ new Date().getFullYear() }}
              <ExternalLink :href="$t('hmc_web_url')" secondary>
                {{ $t("hmc_full_name") }}
              </ExternalLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
