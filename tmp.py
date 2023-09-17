csprings_q_df = pd.read_csv(
    BytesIO(csprings_url_response.content),
    comment="#",
    delimiter="\t",
    skiprows=[27, 28],
    names=["agency_cd", "site_no", "datetime", "streamflow_cfs", "code"],
    index_col="datetime",
    parse_dates=True,
)

csprings_q_df