<script setup>
const assetStats = [
  {
    label: 'Total Assets',
    value: '1,248',
    delta: '+7.3%',
    tone: 'up',
  },
  {
    label: 'Critical Vulnerabilities',
    value: '23',
    delta: '-2.1%',
    tone: 'down',
  },
  {
    label: 'Open Scan Tasks',
    value: '41',
    delta: '+5 new',
    tone: 'up',
  },
  {
    label: 'Resolved This Week',
    value: '87',
    delta: '+14.6%',
    tone: 'up',
  },
]
</script>

<template>
  <main class="dashboard">
    <header class="dashboard__header">
      <p class="dashboard__eyebrow">Security Operations</p>
      <h1>Recon Asset & Vulnerability Dashboard</h1>
    </header>

    <section class="stats-grid" aria-label="Asset statistics">
      <article v-for="stat in assetStats" :key="stat.label" class="stat-card">
        <p class="stat-card__label">{{ stat.label }}</p>
        <p class="stat-card__value">{{ stat.value }}</p>
        <p class="stat-card__delta" :class="`stat-card__delta--${stat.tone}`">{{ stat.delta }}</p>
      </article>
    </section>
  </main>
</template>
