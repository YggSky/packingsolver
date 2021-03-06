#pragma once

#include "packingsolver/algorithms/common.hpp"

#include <set>

namespace packingsolver
{

struct AStarOptionalParameters
{
    Counter thread_id = 0;
    Info info = Info();
};

struct AStarOutput
{
    Counter node_number = 0;
};

template <typename Instance, typename Solution, typename BranchingScheme>
inline AStarOutput a_star(
        const BranchingScheme& branching_scheme,
        SolutionPool<Instance, Solution>& solution_pool,
        AStarOptionalParameters parameters = {})
{
    typedef typename BranchingScheme::Node Node;
    typedef typename BranchingScheme::Insertion Insertion;

    LOG_FOLD_START(parameters.info, "astar" << std::endl);
    AStarOutput output;

    // Initialize queue.
    std::multiset<std::shared_ptr<const Node>, decltype(branching_scheme)> q(branching_scheme);
    q.insert(branching_scheme.root());

    while (!q.empty()) {
        output.node_number++;
        LOG_FOLD_START(parameters.info, "node_number " << output.node_number << std::endl);

        // Check time.
        if (!parameters.info.check_time()) {
            LOG_FOLD_END(parameters.info, "");
            break;
        }

        // Get node from the queue.
        auto node_cur = *q.begin();
        q.erase(q.begin());

        // Bound.
        if (branching_scheme.bound(*node_cur, solution_pool.worst())) {
            LOG(parameters.info, " bound ×" << std::endl);
            continue;
        }

        for (const Insertion& insertion: branching_scheme.insertions(node_cur, parameters.info)) {
            auto child = branching_scheme.child(node_cur, insertion);

            // Bound.
            if (branching_scheme.bound(*child, solution_pool.worst())) {
                LOG(parameters.info, " bound ×" << std::endl);
                continue;
            }

            // Update best solution.
            if (branching_scheme.better(*child, solution_pool.worst())) {
                std::stringstream ss;
                ss << "A* (thread " << parameters.thread_id << ")";
                solution_pool.add(branching_scheme.to_solution(*child, solution_pool.worst()), ss, parameters.info);
            }

            // Add child to the queue.
            if (!branching_scheme.leaf(*child))
                q.insert(child);
        }

        LOG_FOLD_END(parameters.info, "");
    }

    std::stringstream ss;
    ss << "A* (thread " << parameters.thread_id << ")";
    PUT(parameters.info, ss.str(), "NodeNumber", output.node_number);
    LOG_FOLD_END(parameters.info, "");
    return output;
}

}

