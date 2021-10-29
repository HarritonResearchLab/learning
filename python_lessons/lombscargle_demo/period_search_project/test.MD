```{toggle} Don't peak!
:class: dropdown

periodic_ids = np.array([])
best_periods = np.array([])
best_powers = np.array([])

for id in ids: 
    data_df = pd.read_csv(root_dir+r'\\light_curves\\'+id+'_r.csv')
    mjds = np.array(data_df['mjd'])
    mags = np.array(data_df['mag'])

    ls = LombScargle(mjds, mags)
    frequencies, powers = ls.autopower(minimum_frequency=0.05, maximum_frequency=0.5)
    periods = 1/frequencies

    best_period, best_power = periods[np.argmax(powers)], np.max(powers)

    if best_power > 0.5: 
        periodic_ids = np.append(periodic_ids, id)
        best_periods = np.append(best_periods, best_period)
        best_powers = np.append(best_powers, best_power)

        phased_dates = np.mod(mjds, best_period)/best_period

        plt.rcParams['font.family']='serif'
        plt.style.use('ggplot')
        plt.scatter(phased_dates, mags)
        plt.xlabel('Phase (P='+str(round(best_period, 3))+')')
        plt.ylabel('mag')
        plt.gca().invert_yaxis()
        plt.show()

plt.rcParams['font.family']='serif'
plt.style.use('ggplot')
plt.xlabel('Period')
plt.ylabel('Frequency')
plt.title('Distribution of Significant Periods')
plt.hist(best_periods)
plt.savefig('period_dist.png')
```