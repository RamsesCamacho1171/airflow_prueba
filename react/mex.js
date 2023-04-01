import React from "react";
import {
  ComposableMap,
  Geographies,
  Geography,
  Annotation,
  ZoomableGroup
} from "react-simple-maps";

const url="/topo.json"

const Mex = () => {
  return (
    <ComposableMap
      projection="geoAzimuthalEqualArea"
      projectionConfig={{
       rotate:[80,1,0],
        center: [-20, 20],
        scale: 850
      }}
    >
      <Geographies
        geography={url}
        
        stroke="#FFFFFF"
        strokeWidth={0.8}
      >
        {({ geographies }) =>
          geographies.map((geo) => ( 
            <>
                <>{console.log(geo.properties.state_name)}</>
                <Geography key={geo.rsmKey} geography={geo} 
                //console.log() cada vez que se cree este objeto imprima algo en consola
                    style={{
                        default: {
                        fill: "#BBB",
                        },
                        hover: {
                        fill: "#F53",
                        },
                        pressed: {
                        fill: "#E42",
                        },
                    } }
                />
            </>
            
            
            
          ))
        }
        
      </Geographies>

    </ComposableMap>
  );
};

export default Mex;
