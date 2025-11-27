import './App.css'

function App() {

  return (
    <>
      <div className="">
        <h3>Django React</h3>

        <div>
          <label htmlFor="users" className="block text-sm/6 font-medium text-white">
            Nom
          </label>
          <div className="mt-2">
            <div>
              <input
                id="users"
                name="users"
                type="search"
                placeholder="John Doe"
                className=""
              />
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
