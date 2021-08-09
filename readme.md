# Welcome to the Capstone for Python MLOps Bootcamp
### _Bootcamp hosted by [PyLadies Amsterdam] Python and presented by [Dexter]_

## Capstone Description
>Pytown, located in the remote area in the north of the Netherlands, wants to live on 100% renewable energy. Our town has enough solar panels and wind turbines to generate electricity, so we disconnected from the main electricity grid a while ago. However, we usually do not use the electricity at the moment of its generation by sun and/or wind, which is causing daily power blackouts. We are fed up with all the electricity problems and ask your team to support us. Help us to adjust our electricity demand to the electricity generation.

We want to have a dashboard telling us when it is allowed to use electricity as much as we want, use less electricity or charge only essential devices.

## Solution Description
We took a iterative approach to have an end-to-end system from the first iteration.
1. **Data preprocessing**: daily aggregation of: 
- energy load -> energy consumption 
- wind and solar predictions -> energy generation
2. **Model training**: 
- naive forecast: average consumption of the same day of the week, considering N weeks before
- further iterations: try linear regression
3. **Model evaluation**: backtest with a sliding window approach, optimize for MAPE
4. **Model deployment**: deploy the best performing model as an Azure Machine Learning Batch pipeline Model
5. **Model post-processing**: 
    - compare energy consumption forecast with energy generation from wind and solar predictions
    - classify the energy consumption per day (normal, middle, low charge), using consumption distrubtion pattern
    - persist results to Azure Blob Storage to be used by Power BI
6. Build dashboard with recommendations for the energy consumption on the following day

**_Watch our team [presentation] on YouTube._**

## Team

- [Hassan]
- [Dânia]
- Mentor: Matthijs


## Tech

In order to have a dashboard working properly, we developed an end-to-end framework using:

- git
- Docker
- Git bash
- Conda
- Visual Studio Code
- Azure (Storage, Machine Learning, Pipelines, CLI)
- Power BI

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [bootcamp-repo]: <https://github.com/pyladiesams/bootcamp-bringing-ML-models-into-production-intermediary-jun-aug2021>
   [dânia]: <https://www.linkedin.com/in/meiradania/>
   [hassan]: <linkedin.com/in/hassansalamb/>
   [pyladies amsterdam]: <https://amsterdam.pyladies.com/>
   [dexter]: <https://dexterenergy.ai/>
   [presentation]: <https://youtu.be/aLReepA68Nk>