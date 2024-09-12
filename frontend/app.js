document.addEventListener("DOMContentLoaded", function () {
  const chartType = document.getElementById("chart-type");
  const chartContainer = document.getElementById("main");

  // Initialisation du graphique
  let chart = echarts.init(chartContainer);

  // Fonction pour réinitialiser le graphique
  function resetChart() {
    if (chart) {
      chart.dispose(); // Détruit l'ancien graphique
    }
    chart = echarts.init(chartContainer); // Crée un nouveau graphique
  }

  // Fonction pour récupérer toutes les pages de données
  async function fetchAllData() {
    let url = `http://localhost:8000/api/pokemons`;
    let page = 1;
    let allData = [];
    let totalPages;

    try {
      do {
        const response = await fetch(`${url}?page=${page}&size=50`);
        const data = await response.json();
        allData = allData.concat(data.items);
        totalPages = data.pages;
        page++;
      } while (page <= totalPages);

      return allData;
    } catch (error) {
      console.error("Error fetching data:", error);
      return [];
    }
  }

  // Fonction pour mettre à jour le graphique
  function updateChart(data) {
    resetChart(); 
    const selectedChartType = chartType.value;
    let option = {};

    switch (selectedChartType) {
      case "pie":
        // Compter les occurrences de chaque type
        const typeCounts = {};

        data.forEach((item) => {
          item.types.forEach((type) => {
            if (typeCounts[type]) {
              typeCounts[type] += 1;
            } else {
              typeCounts[type] = 1;
            }
          });
        });

        // Convertir l'objet typeCounts en un tableau pour ECharts
        const pieData = Object.keys(typeCounts).map((type) => {
          return { name: type, value: typeCounts[type] };
        });

        option = {
          title: { text: "Pokemon Type Distribution" },
          tooltip: { trigger: "item" },
          series: [
            {
              name: "Type",
              type: "pie",
              data: pieData,
            },
          ],
        };
        break;

      case "scatter":
        option = {
          title: { text: "Attack vs. Defense" },
          tooltip: { trigger: "item" },
          xAxis: { type: "value", name: "Attack" },
          yAxis: { type: "value", name: "Defense" },
          series: [
            {
              name: "Pokemon",
              type: "scatter",
              data: data.map((item) => [item.attack, item.defense]),
            },
          ],
        };
        break;

      case "radar":
        // Calcul des moyennes des stats par type
        const statsByType = {};
        data.forEach((item) => {
          item.types.forEach((type) => {
            if (!statsByType[type]) {
              statsByType[type] = { hp: 0, attack: 0, defense: 0, attack_special: 0, defense_special: 0, speed: 0, count: 0 };
            }
            statsByType[type].hp += item.hp;
            statsByType[type].attack += item.attack;
            statsByType[type].defense += item.defense;
            statsByType[type].attack_special += item.attack_special;
            statsByType[type].defense_special += item.defense_special;
            statsByType[type].speed += item.speed;
            statsByType[type].count += 1;
          });
        });

        const radarData = Object.keys(statsByType).map((type) => {
          const stats = statsByType[type];
          return {
            value: [
              stats.hp / stats.count,
              stats.attack / stats.count,
              stats.defense / stats.count,
              stats.attack_special / stats.count,
              stats.defense_special / stats.count,
              stats.speed / stats.count,
            ],
            name: type,
          };
        });

        option = {
          title: { text: "Statistical Averages by Type"},
          tooltip: {},
          legend: {
            data: Object.keys(statsByType),
            selectedMode: "multiple",
            top: 30,
          },
          radar: {
            indicator: [
              { name: "HP", max: 150 },
              { name: "Attack", max: 150 },
              { name: "Defense", max: 150 },
              { name: "Special Attack", max: 150 },
              { name: "Special Defense", max: 150 },
              { name: "Speed", max: 150 },
            ],
          },
          series: [
            {
              name: "Average Stats",
              type: "radar",
              data: radarData,
            },
          ],
        };
        break;
    }

    // Applique la configuration au graphique
    chart.setOption(option);
  }

  // Écouteur d'événements pour le changement du type de graphique
  chartType.addEventListener("change", () => {
    fetchAllData().then(updateChart);
  });

  // Récupère les données et affiche le graphique initial
  fetchAllData().then(updateChart);
});
