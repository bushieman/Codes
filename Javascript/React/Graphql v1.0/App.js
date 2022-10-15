import express from "express";
import { graphqlHTTP } from "express-graphql";
import {
  GraphQLInt,
  GraphQLSchema,
  GraphQLString,
  GraphQLObjectType,
  GraphQLList,
  GraphQLNonNull,
} from "graphql";
const app = express();
const port = process.env.PORT || 4000;

const users = [
  {
    id: 1,
    username: "Norma_Parker31",
    email: "Fleta.Ernser90@gmail.com",
    bio:
      "I'll bypass the solid state TCP capacitor, that should alarm the SQL protocol!",
  },
  {
    id: 2,
    username: "Christine.Mann33",
    email: "Peggie_Dooley92@hotmail.com",
    bio:
      "I'll back up the open-source PNG alarm, that should interface the SQL port!",
  },
  {
    id: 3,
    username: "Barbara29",
    email: "Marlon_Kulas@hotmail.com",
    bio:
      "You can't back up the pixel without synthesizing the neural SSL card!",
  },
  {
    id: 4,
    username: "Jose.Dickens",
    email: "Sonia_Farrell@gmail.com",
    bio:
      "Try to parse the JSON bandwidth, maybe it will generate the open-source matrix!",
  },
  {
    id: 5,
    username: "Janis_Smith13",
    email: "Amara_Goyette32@gmail.com",
    bio:
      "You can't synthesize the capacitor without parsing the auxiliary EXE alarm!",
  },
  {
    id: 6,
    username: "Kelton3",
    email: "Ayden.Bogan75@gmail.com",
    bio: "We need to input the auxiliary EXE capacitor!",
  },
  {
    id: 7,
    username: "Heber70",
    email: "Jaime17@gmail.com",
    bio:
      "backing up the bandwidth won't do anything, we need to back up the multi-byte COM feed!",
  },
  {
    id: 8,
    username: "Ima.Weissnat98",
    email: "Breanne.Bergstrom@hotmail.com",
    bio:
      "The SMTP interface is down, override the mobile capacitor so we can synthesize the IB transmitter!",
  },
  {
    id: 9,
    username: "Tiana.Wilkinson",
    email: "Candelario.Murray@yahoo.com",
    bio:
      "The XML protocol is down, connect the virtual application so we can compress the SAS program!",
  },
  {
    id: 10,
    username: "Justine28",
    email: "Jamison_Lindgren58@gmail.com",
    bio:
      "Use the primary THX transmitter, then you can parse the 1080p matrix!",
  },
];

//define the usertype
const UserType = new GraphQLObjectType({
  name: "UserType",
  description: "User type details",
  fields: () => ({
    id: { type: GraphQLNonNull(GraphQLInt) },
    username: { type: GraphQLNonNull(GraphQLString) },
    email: { type: GraphQLNonNull(GraphQLString) },
    bio: { type: GraphQLNonNull(GraphQLString) },
  }),
});

//query the root
const RootQuery = new GraphQLObjectType({
  name: "QueryType",
  description: "Root Query",
  fields: () => ({
    getAllUsers: {
      type: new GraphQLList(UserType),
      description: "list of all users",
      resolve: () => users,
    },
  }),
});

//query the create, read , update and delete
const Mutation = new GraphQLObjectType({
  name: "Mutation",
  description: "read data",
  fields: () => ({
    getUser: {
      type: UserType,
      description: "get a single user with specific id",
      args: {
        id: { type: GraphQLNonNull(GraphQLInt) },
      },
      resolve: (parent, args) => users.find((user) => user.id === args.id),
    },
    addUser: {
      type: UserType,
      description: "create a new user",
      args: {
        id: { type: GraphQLInt },
        username: { type: GraphQLNonNull(GraphQLString) },
        email: { type: GraphQLNonNull(GraphQLString) },
        bio: { type: GraphQLNonNull(GraphQLString) },
      },
      resolve: (parent, args) => {
        const newUser = {
          id: users.length + 1,
          username: args.username,
          email: args.email,
          bio: args.bio,
        };
        users.push(newUser);
        return newUser;
      },
    },
    //couldnot get the object to update on the array
    updateUser: {
      type: UserType,
      description: "update an existing user",
      args: {
        id: { type: GraphQLNonNull(GraphQLInt) },
        username: { type: GraphQLNonNull(GraphQLString) },
        email: { type: GraphQLNonNull(GraphQLString) },
        bio: { type: GraphQLNonNull(GraphQLString) },
      },
      resolve: (parent, args) => {
        let existingUser = users.find((user) => user.id === args.id);
        if (!existingUser) return console.log("user not found");
        const updatedUser = {
          id: args.id,
          username: args.username,
          email: args.email,
          bio: args.bio,
        };
        existingUser = updatedUser;
        return existingUser;
      },
    },
    deleteUser: {
      type: UserType,
      description: "deleting an existing user",
      args: {
        id: { type: GraphQLNonNull(GraphQLInt) },
      },
      resolve: (parent, args) => {
        let existingUser = users.find((user) => user.id === args.id);
        if (!existingUser) return console.log("user not found");
        const index = users.indexOf(existingUser);
        users.splice(index, 1);
        return existingUser;
      },
    },
  }),
});

//defining the schema
const schema = new GraphQLSchema({
  query: RootQuery,
  mutation: Mutation,
});

app.use(
  "/graphql",
  graphqlHTTP({
    schema,
    graphiql: true,
  })
);

app.listen(port, console.log(`listening on pert ${port}...`));
