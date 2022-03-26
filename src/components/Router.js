import useState from "react";
import {HashRouter as Router, Route, Routes} from "react-router-dom";
import Home from "../routes/Home";
import Auth from "../routes/Auth";
const AppRouter = () => {
	const [isloggedin, setisloggedin] = useState(false);
	return (
		<Router>
			<Routes>
				{isloggedin ? (
					<Route path="/" element={<Home />} />
				) : (
					<Route path="/" element={<Auth />} />
				)}
			</Routes>
		</Router>
	);
};

export default AppRouter;