import React, { useState } from "react";

import algoliasearch from "algoliasearch/lite";
import {
	InstantSearch,
	SearchBox,
	Hits,
	connectHighlight,
} from "react-instantsearch-dom";

const searchClient = algoliasearch(
	"8PU2WDR4HM",
	"de2aac149a9c6f99560662c696f667f8"
);

function App() {
	const [query, setQuery] = useState("");

	const Hit = ({ hit }) => (
		<p>
			<CustomHighlight attribute="bio" hit={hit} />
		</p>
	);

	const CustomHighlight = connectHighlight(({ highlight, attribute, hit }) => {
		const parsedHit = highlight({
			highlightProperty: "_highlightResult",
			attribute,
			hit,
		});

		return (
			<div>
				<h3>{hit.username}</h3>
				<img src={hit.avatar} alt={hit.username} />
				{parsedHit.map((part) =>
					part.isHighlighted ? <mark>{part.value}</mark> : part.value
				)}
			</div>
		);
	});

	return (
		<InstantSearch searchClient={searchClient} indexName="customers">
			<SearchBox onChange={(e) => setQuery(e.target.value)} />
			<div>{!query ? "" : <Hits hitComponent={Hit} />}</div>
		</InstantSearch>
	);
}

export default App;
