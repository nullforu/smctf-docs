// @ts-check
import { defineConfig } from 'astro/config'
import starlight from '@astrojs/starlight'

// https://astro.build/config
export default defineConfig({
    site: 'https://ctf.null4u.cloud',
    // base: '/smctf-docs',
    integrations: [
        starlight({
            title: 'SMCTF Docs',
            social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/nullforu/smctf' }],
            sidebar: [
                {
                    label: 'CHANGELOG',
                    autogenerate: { directory: 'changelog' },
                },
                {
                    label: 'SMCTF',
                    autogenerate: { directory: 'smctf' },
                },
                {
                    label: 'Container Provisioner',
                    autogenerate: { directory: 'container-provisioner' },
                },
                {
                    label: 'Infrastructure',
                    autogenerate: { directory: 'infra' },
                },
                {
                    label: 'Reference',
                    autogenerate: { directory: 'reference' },
                },
                {
                    label: 'FAQ & Troubleshooting',
                    autogenerate: { directory: 'faq' },
                },
            ],
        }),
    ],
})
